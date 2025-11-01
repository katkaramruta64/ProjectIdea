// --- Tab Switching ---
function openTab(evt, tabName) {
    let tabcontent = document.getElementsByClassName("tab-content");
    for (let i = 0; i < tabcontent.length; i++) tabcontent[i].style.display = "none";
    let tablinks = document.getElementsByClassName("tablink");
    for (let i = 0; i < tablinks.length; i++) tablinks[i].classList.remove("active");
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.classList.add("active");
}

// --- API Search ---
let allPapers = [];
let currentIndex = 0;
const pageSize = 5;

async function searchPapers() {
    const query = document.getElementById("query").value || "ai";
    if (!navigator.onLine) {
        document.getElementById("api-results").innerHTML = `<p style="color:red;"> No internet</p>`;
        return;
    }

    try {
        const response = await fetch(`/get-papers?query=${query}`);
        const data = await response.json();
        allPapers = data.papers || [];
        currentIndex = 0;

        if (allPapers.length === 0) {
            document.getElementById("api-results").innerHTML = `<p style="color:red;"> No papers found</p>`;
            return;
        }

        document.querySelector("button[onclick*='results']").click();
        showPage();

    } catch (err) {
        console.error("Error:", err);
        document.getElementById("api-results").innerHTML = `<p style="color:red;"> Failed to fetch papers</p>`;
    }
}

function showPage() {
    const resultsDiv = document.getElementById("api-results");
    resultsDiv.innerHTML = "";

    const pagePapers = allPapers.slice(currentIndex, currentIndex + pageSize);

    pagePapers.forEach(paper => {
        const paperDiv = document.createElement("div");
        paperDiv.className = "idea-card";

        paperDiv.innerHTML = `
            <h3><a href="${paper.link}" target="_blank">${paper.title}</a></h3>
            <div class="abstract"><strong>Abstract:</strong> ${paper.summary}</div>
            <div class="idea-highlight"><strong>💡 Suggested Project Idea:</strong> <b>${paper.suggested_idea}</b></div>
            <button class="save-btn"
                data-title="${encodeURIComponent(paper.title)}"
                data-idea="${encodeURIComponent(paper.suggested_idea)}"
                data-link="${encodeURIComponent(paper.link)}"
                onclick="saveIdea(this)">Save</button>
        `;

        resultsDiv.appendChild(paperDiv);
    });

    document.getElementById("pagination").style.display = "flex";
    document.getElementById("prevBtn").disabled = currentIndex === 0;
    document.getElementById("nextBtn").disabled = currentIndex + pageSize >= allPapers.length;
}

function showNext() { if (currentIndex + pageSize < allPapers.length) { currentIndex += pageSize; showPage(); } }
function showPrev() { if (currentIndex - pageSize >= 0) { currentIndex -= pageSize; showPage(); } }

// --- Save & Remove Ideas ---
let savedTitles = new Set();

function saveIdea(button) {
    const title = decodeURIComponent(button.getAttribute("data-title"));
    const idea = decodeURIComponent(button.getAttribute("data-idea"));
    const link = decodeURIComponent(button.getAttribute("data-link"));

    if (savedTitles.has(title)) {
        alert("⚠️ This idea is already saved!");
        return;
    }

    savedTitles.add(title);
    const savedList = document.getElementById("saved-list");

    const savedDiv = document.createElement("div");
    savedDiv.className = "idea-card";

    savedDiv.innerHTML = `
        <h3><a href="${link}" target="_blank">${title}</a></h3>
        <div class="abstract"><strong>💡 Suggested Idea:</strong> ${idea}</div>
        <button class="action-btn remove-btn">Remove</button>
    `;

    const removeBtn = savedDiv.querySelector(".remove-btn");
    removeBtn.addEventListener("click", () => {
        savedTitles.delete(title);
        savedDiv.remove();
    });

    savedList.appendChild(savedDiv);

    // --- Fix: Properly switch tabs ---
    // Hide all tabs
    document.querySelectorAll(".tab-content").forEach(tab => tab.style.display = "none");
    // Remove active class from all buttons
    document.querySelectorAll(".tablink").forEach(btn => btn.classList.remove("active"));

    // Show Saved tab and mark its button as active
    document.getElementById("saved").style.display = "block";
    document.querySelector("button[onclick*='saved']").classList.add("active");
}
