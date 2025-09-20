import itertools

DOMAIN_NAMES = {
    "computer_science": "Computer Science",
    "electronics": "Electronics & Communication",
    "mechanical": "Mechanical Engineering",
    "civil": "Civil Engineering",
    "energy": "Energy & Power Systems",
    "healthcare": "Healthcare & Biomedical",
    "agriculture": "Agriculture & Food Technology",
    "management": "Management & Business",
    "education": "Education & E-Learning",
    "environment": "Environmental Science & Sustainability"
}

TEMPLATES = [
    "Design an AI/ML model inspired by '{title}' for {domain}.",
    "Develop a novel application of '{title}' in {domain}.",
    "Extend the ideas of '{title}' to build practical {domain} solutions.",
    "Create a project applying '{title}' concepts for {domain} innovation.",
    "Use '{title}' as the foundation for an AI-based {domain} system.",
    "Implement a real-world solution by adapting '{title}' in {domain}.",
    "Explore how '{title}' can enhance {domain} using AI/ML.",
    "Build a prototype inspired by '{title}' for advancements in {domain}."
]

# Round-robin cycle for templates
template_cycle = itertools.cycle(TEMPLATES)

# Keywords to detect special themes
KEYWORDS = {
    "deep learning": "using deep learning techniques",
    "machine learning": "leveraging machine learning models",
    "neural network": "with neural network architectures",
    "renewable": "to promote renewable energy",
    "sustainability": "for sustainability solutions",
    "climate": "to address climate challenges",
    "iot": "with IoT-based innovations",
    "blockchain": "using blockchain technology",
    "agriculture": "to improve smart farming",
    "health": "for improving healthcare services",
    "education": "to support personalized education"
}

def clean_title(title, max_words=15):
    words = title.split()
    if len(words) > max_words:
        return " ".join(words[:max_words]) + "..."
    return title

def extract_context(summary):
    summary_lower = summary.lower()
    for keyword, phrase in KEYWORDS.items():
        if keyword in summary_lower:
            return phrase
    return None

def generate_project_idea(title, summary, domain="computer_science"):
    short_title = clean_title(title)
    domain_name = DOMAIN_NAMES.get(domain, domain.replace("_", " ").title())

    template = next(template_cycle)
    base_idea = template.format(title=short_title, domain=domain_name)

    # Add context if found
    context_phrase = extract_context(summary)
    if context_phrase:
        return f": {base_idea} ({context_phrase})."
    else:
        return f"; {base_idea}"