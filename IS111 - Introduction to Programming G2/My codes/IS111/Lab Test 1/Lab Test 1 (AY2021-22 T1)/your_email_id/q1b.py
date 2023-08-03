# Name:
# Email ID:

def is_official_language(country, language):
    # Replace the code below with your implementation.
    belgium = ("Dutch", "French", "German")
    canada = ("English", "French")
    philippines = ("English", "Filipino")
    singapore = ("Chinese", "English", "Malay", "Tamil")

    if country == "Belgium":
        if language in belgium:
            return True
        else:
            return False
    
    if country == "Canada":
        if language in canada:
            return True
        else:
            return False
    
    if country == "Philippines":
        if language in philippines:
            return True
        else:
            return False
    
    if country == "Singapore":
        if language in singapore:
            return True
        else:
            return False