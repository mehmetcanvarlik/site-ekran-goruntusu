from html2image import Html2Image

html = Html2Image()

website ="https://www.sovitalvitamins.com"

output_file = "medium.png"

html.screenshot(url=website, save_as=output_file)
