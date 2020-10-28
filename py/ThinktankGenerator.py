import os

# Template for game preview
PREVIEWTEMPLATE = "<div class='ThinktankIdea'>\
    <h3>%%IDEANAME%%</h3>\
    <p>%%IDEASUMMARY%%</p>\
    <a href='#' onclick='loadpage(\"%%IDEAPATH%%\")'>read more</a>\
</div>\
<div class='gamePreviewBreak'></div>"

# Start line of HTML code
HTMLSTARTER = "<div style='margin:0 auto; min-width:100%; max-width: 100%;'>"

# End line of HTML code
HTMLENDER = "</div>"

### Takes the template and variables and fills in the tokens as needed
def FillTokens(PreviewTemplate, IdeaName, PreviewText, IdeaLink):

    # Implants idea's name
    PreviewTemplate = PreviewTemplate.replace("%%IDEANAME%%", IdeaName)
        
    # Implants preview text
    PreviewTemplate = PreviewTemplate.replace("%%IDEASUMMARY%%", PreviewText)

    # Implants idea link path
    PreviewTemplate = PreviewTemplate.replace("%%IDEAPATH%%", IdeaLink)

    # Returns completed preview
    return PreviewTemplate

### Finds the data needed to fill tokens in the template
def GetData(IdeaName):

    # Creates path for idea link
    game_path = ("thinktankIdeas\\\\" + IdeaName)
    
    # Finds path to preview content file
    preview_path = ("C:\\source\\jackportfolio\\pages\\thinkTankIdeas\\previews\\" + IdeaName + ".txt")

    # Opens appropriate preview file
    with open(preview_path,"r") as preview_file:

        # Reads content of preview file
        preview_content = preview_file.read()

        # Closes file
        preview_file.close()

    # Returns game link path, and preview content
    return game_path, preview_content

### Writes HTML into thinktank page file
def WriteToGamesPage(HtmlContent):
    
    # Opens thinktank page file
    with open("C:\\source\\jackportfolio\\pages\\thinktank.html", "w") as blog_page:

        # Overwrites file with new HTML content to display
        blog_page.write(HtmlContent)

        # Closes file
        blog_page.close()

### Puts the HTML content together
def HtmlSticher(PreviewTemplate, StartLine, EndLine):
    
    # Empty HTML content
    html_content = ""

    # Adds starting line to the HTML content
    html_content += StartLine

    # Finds all ideas in thinktank idea folder
    ideas = [name for name in os.listdir('C:\\source\\jackportfolio\\pages\\thinkTankIdeas')]
    
    # Orders all ideas in date order, newest first
    ideas.sort(reverse = True)

    # Itterates through every idea
    for each_name in ideas:

        # Turns each idea name into a string, just in case
        each_name = str(each_name)

        # Only perform the rest of the loop if the idea isn't actually just the preview folder
        if each_name != "previews":

            # Strips idea name of extension for use with functions
            each_name = each_name.replace(".html",'')
        
            # Calls function to get the required data for the idea preview
            game_path, preview_content = GetData(each_name)

            # Calls function to get filled template for that idea preview
            game_preview = FillTokens(PreviewTemplate, each_name, preview_content, game_path)

            # Adds preview for idea into html content
            html_content += game_preview
    
    # Adds closing line of content
    html_content += EndLine

    # Calls function to save content into thinktank page
    WriteToGamesPage(html_content)


HtmlSticher(PREVIEWTEMPLATE,HTMLSTARTER,HTMLENDER)