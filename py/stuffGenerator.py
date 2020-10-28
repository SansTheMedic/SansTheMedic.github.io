import os

# Start line of HTML code
HTMLSTARTER = "<div style='margin:0 auto; min-width:100%; max-width: 100%;'>"

# End line of HTML code
HTMLENDER = "</div>"

# HTML template of documents
DOCTEMPLATE = "<div class='stuffDocBlock'>\
    <div class='stuffDocIconBlock'>\
            <img class='stuffDocIcon' src='%%ICONPATH%%'>\
    </div>\
    <div class='stuffDocPreview'>\
        %%PREVIEWCONTENT%%\
        <a href='#' onclick='loadpage(\"%%DOCPATH%%\",null)'>See here</a>\
    </div>\
</div>\
<div class='stuffBreak'></div>"

# HTML template of images
IMAGETEMPLATE = "<div class='stuffImageBlock'>\
    <div class='stuffImageHeader'>\
        <h3>%%HEADER%%</h3>\
    </div>\
    <div class='stuffImage'>\
        <img src='%%IMAGEPATH%%' width='100%'>\
    </div>\
</div>\
<div class='stuffBreak'></div>"


### Gets data for image previews (really just the image path)
def getImageData(ImageName):
    
    # Gets path for image
    image_path = ("\\images\\stuffImages\\" + ImageName + ".png")

    # Returns the image path
    return image_path


### Gets data for document previews
def getDocData(DocName):
    
    # Creates path for image
    image_path = ("\\images\\stuffIcons\\" + DocName + ".png")

    # Creates path for doc link
    doc_path = ("stuffDocs\\\\" + DocName)
    
    # Finds path to preview content file
    preview_path = ("C:\\source\\jackportfolio\\pages\\stuffDocs\\previews\\" + DocName + ".txt")

    # Opens appropriate preview file
    with open(preview_path,"r") as preview_file:

        # Reads content of preview file
        preview_content = preview_file.read()

        # Closes file
        preview_file.close()

    # Returns image path, doc link path, and preview content
    return image_path, doc_path, preview_content



### Fills in tokens for image preview
def fillImageTemplate(PreviewTemplate, ImageHeader, ImagePath):

    # Implants header
    PreviewTemplate = PreviewTemplate.replace("%%HEADER%%", ImageHeader)

    # Implants image path
    PreviewTemplate = PreviewTemplate.replace("%%IMAGEPATH%%", ImagePath)

    # Returns preview
    return PreviewTemplate


### Fills in tokens for document preview
def fillDocTemplate(PreviewTemplate, IconLink, PreviewText, DocLink):

    # Implants icon path
    PreviewTemplate = PreviewTemplate.replace("%%ICONPATH%%", IconLink)

    # Implants preview text and heading
    PreviewTemplate = PreviewTemplate.replace("%%PREVIEWCONTENT%%", PreviewText)

    # Implants article link path
    PreviewTemplate = PreviewTemplate.replace("%%DOCPATH%%", DocLink)

    # Returns completed preview
    return PreviewTemplate


### Writes HTML into stuff page file
def WriteToStuffPage(HtmlContent):
    
    # Opens thinktank page file
    with open("C:\\source\\jackportfolio\\pages\\stuff.html", "w") as blog_page:

        # Overwrites file with new HTML content to display
        blog_page.write(HtmlContent)

        # Closes file
        blog_page.close()


### Finds all images and pages to put in
def getFiles():
    
    # Gets all document files
    document_files = [name for name in os.listdir('C:\\source\\jackportfolio\\pages\\stuffDocs')]

    # Gets all image files
    image_files = [name for name in os.listdir('C:\\source\\jackportfolio\\images\\stuffImages')]

    # Empty list to put all files into
    all_files = []

    # Adds document files to list of all files, adding pointer that they're documents
    for each_doc in document_files:

        # Turns each article name into a string, just in case
        each_doc = str(each_doc)

        # Removes extension
        each_doc = each_doc.replace(".html",'')

        # Adds to list with document pointer
        all_files.append([each_doc,"document"])
    
    # Adds image files to list of all files, adding pointer that they're images
    for each_image in image_files:

        # Turns each article name into a string, just in case
        each_image = str(each_image)

        # Removes extension
        each_image = each_image.replace(".png",'')

        # Adds to list with document pointer
        all_files.append([each_image,"image"])

    # Returns all files
    return all_files


### Puts HTML content together
def HtmlStitcher(StartLine, EndLine, ImageTemplate, DocTemplate):

    # Empty HTML content
    html_content = ""

    # Adds starting line to the HTML content
    html_content += StartLine

    # Gets all files to be put into the page
    all_files = getFiles()

    # Orders files, newest first
    all_files.sort(reverse=True)

    # Iterates through all files
    for each_file in all_files:

        # Does not add anything if the file is the document previews folder
        if each_file[0] != "previews":

            # Adds image display
            if each_file[1] == "image":

                # Gets data for image display
                image_path = getImageData(each_file[0])

                # Fills in tokens for template of image display
                file_display = fillImageTemplate(ImageTemplate, each_file[0], image_path)
            
            # Adds document preview
            else:

                # Gets data for document preview
                image_path, doc_path, preview_content = getDocData(each_file[0])

                # Fills in tokens for template of document preview
                file_display = fillDocTemplate(DocTemplate, image_path, preview_content, doc_path)
            
            # Adds new item to html content
            html_content += file_display
    
    # Adds end line to html content
    html_content += EndLine

    # Writes html to stuff page
    WriteToStuffPage(html_content)


HtmlStitcher(HTMLSTARTER, HTMLENDER, IMAGETEMPLATE, DOCTEMPLATE)
