from google_images_download import google_images_download
import sys

busca = sys.argv[1]
limit = sys.argv[2]

response = google_images_download.googleimagesdownload()

arguments = {"keywords": busca, "limit": limit, "delay":1, "outpu_directory":"train", "print_url": True, "prefix": busca}
paths = response.download(arguments)

print(paths)
