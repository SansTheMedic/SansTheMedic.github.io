import os

# Template for game preview
PREVIEWTEMPLATE = "<div class='gamePreview'> \
        <h1> \
            <a href='#' onclick='loadpage(\"%%GAMEPATH%%\",null)'> \
                %%GAMENAME%% \
            </a> \
        </h1> \
        <p>%%PREVIEWCONTENT%%</p> \
    </div>\
    <div class='gamePreviewBreak'></div>"

# Start line of HTML code
HTMLSTARTER = "<div style='margin:0 auto; min-width:100%; max-width: 100%;'>"

# End line of HTML code
HTMLENDER = "</div>"

### Takes the template and variables and fills in the tokens as needed
def FillTokens(PreviewTemplate, GameName, PreviewText, GameLink):

    # Implants game's name
    PreviewTemplate = PreviewTemplate.replace("%%GAMENAME%%", GameName)
        
    # Implants preview text
    PreviewTemplate = PreviewTemplate.replace("%%PREVIEWCONTENT%%", PreviewText)

    # Implants game link path
    PreviewTemplate = PreviewTemplate.replace("%%GAMEPATH%%", GameLink)

    # Returns completed preview
    return PreviewTemplate

### Finds the data needed to fill tokens in the template
def GetData(GameName):

    # Creates path for game link
    game_path = ("gamesPages\\\\" + GameName)
    
    # Finds path to preview content file
    preview_path = ("C:\\Users\\jackwork\\Documents\\GitHub\\SansTheMedic.github.io\\pages\\gamesPages\\previews\\" + GameName + ".txt")

    # Opens appropriate preview file
    with open(preview_path,"r") as preview_file:

        # Reads content of preview file
        preview_content = preview_file.read()

        # Closes file
        preview_file.close()

    # Returns game link path, and preview content
    return game_path, preview_content

### Writes HTML into games page file
def WriteToGamesPage(HtmlContent):
    
    # Opens thinktank page file
    with open("C:\\Users\\jackwork\\Documents\\GitHub\\SansTheMedic.github.io\\pages\\games.html", "w") as blog_page:

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

    # Finds all Games in Game folder
    games = [name for name in os.listdir('C:\\Users\\jackwork\\Documents\\GitHub\\SansTheMedic.github.io\\pages\\gamesPages')]
    
    # Orders all games in date order, newest first
    games.sort(reverse = True)

    # Itterates through every game
    for each_name in games:

        # Turns each game name into a string, just in case
        each_name = str(each_name)

        # Only perform the rest of the loop if the game isn't actually just the preview folder
        if each_name != "previews":

            # Strips game name of extension for use with functions
            each_name = each_name.replace(".html",'')
        
            # Calls function to get the required data for the game preview
            game_path, preview_content = GetData(each_name)

            # Calls function to get filled template for that game preview
            game_preview = FillTokens(PreviewTemplate, each_name, preview_content, game_path)

            # Adds preview for game into html content
            html_content += game_preview
    
    # Adds closing line of content
    html_content += EndLine

    # Calls function to save content into games page
    WriteToGamesPage(html_content)


HtmlSticher(PREVIEWTEMPLATE,HTMLSTARTER,HTMLENDER)
