# Clay static project settings
# Do not show HTML fragments in the final build or in the _index.html
FILTER_PARTIALS = True

# Folders and files to be ignored when building the static site
FILTER = [
    "*_templates/*",
    "*_tmpl/*"
]

## When building, force the inclusion of all the HTML partials listed here.
## You can use patterns here eg: "alert-*.html"
INCLUDE = [

]

## Server
HOST = '0.0.0.0'
PORT = 8080

## Your own settings here
