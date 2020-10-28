import os

# Template for blog article
ARTICLETEMPLATE = "<div class='blogarticle'> \
        <div class='articleiconblock'> \
            <img class='articleicon' src='%%ICONPATH%%'> \
        </div> \
        <div class='articlepreview'> \
            %%PREVIEWCONTENT%% \
            <a href='#' onclick='loadpage(\"%%ARTICLEPATH%%\",null)'>Read more!</a> \
        </div>\
    </div> \
    <div class='blogarticlebreak'></div>"

# Start line of HTML code
HTMLSTARTER = "<div style='margin:0 auto; min-width:100%; max-width: 100%;'>"

# End line of HTML code
HTMLENDER = "</div>"

### Takes the template and variables and fills in the tokens as needed
def FillTokens(PreviewTemplate, IconLink, PreviewText, ArticleLink):
        
    # Implants icon path
    PreviewTemplate = PreviewTemplate.replace("%%ICONPATH%%", IconLink)

    # Implants preview text and heading
    PreviewTemplate = PreviewTemplate.replace("%%PREVIEWCONTENT%%", PreviewText)

    # Implants article link path
    PreviewTemplate = PreviewTemplate.replace("%%ARTICLEPATH%%", ArticleLink)

    # Returns completed preview
    return PreviewTemplate

### Finds the data needed to fill tokens in the template
def GetData(ArticleName):

    # Creates path for image
    image_path = ("\\images\\blogIcons\\" + ArticleName + ".png")

    # Creates path for article link
    article_path = ("blogArticles\\\\" + ArticleName)
    
    # Finds path to preview content file
    preview_path = ("C:\\source\\jackportfolio\\pages\\blogArticles\\previews\\" + ArticleName + ".txt")

    # Opens appropriate preview file
    with open(preview_path,"r") as preview_file:

        # Reads content of preview file
        preview_content = preview_file.read()

        # Closes file
        preview_file.close()

    # Returns image path, article link path, and preview content
    return image_path, article_path, preview_content

### Writes HTML into blog page file
def WriteToBlogPage(HtmlContent):
    
    # Opens blog page file
    with open("C:\\source\\jackportfolio\\pages\\blog.html", "w") as blog_page:

        # Overwrites file with new HTML content to display
        blog_page.write(HtmlContent)

        # Closes file
        blog_page.close()

### Puts the HTML content together
def HtmlSticher(ArticleTemplate, StartLine, EndLine):
    
    # Empty HTML content
    html_content = ""

    # Adds starting line to the HTML content
    html_content += StartLine

    # Finds all articles in article folder
    articles = [name for name in os.listdir('C:\\source\\jackportfolio\\pages\\blogArticles')]
    
    # Orders all articles in date order, newest first
    articles.sort(reverse = True)

    # Itterates through every article
    for each_name in articles:

        # Turns each article name into a string, just in case
        each_name = str(each_name)

        # Only perform the rest of the loop if the article isn't actually just the preview folder
        if each_name != "previews":

            # Strips article name of extension for use with functions
            each_name = each_name.replace(".html",'')
        
            # Calls function to get the required data for the article preview
            image_path, article_path, preview_content = GetData(each_name)

            # Calls function to get filled template for that article preview
            article_preview = FillTokens(ArticleTemplate, image_path, preview_content, article_path)

            # Adds preview for article into html content
            html_content += article_preview
    
    # Adds closing line of content
    html_content += EndLine

    # Calls function to save content into blog page
    WriteToBlogPage(html_content)


HtmlSticher(ARTICLETEMPLATE,HTMLSTARTER,HTMLENDER)