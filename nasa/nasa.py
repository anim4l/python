import requests

def nasa():
    print "Fetching Image Manifest..."
    data = requests.get('http://json.jpl.nasa.gov/data.json').json()
    mission_url = data["MSL"]["image_manifest"]

    print "Fetching Mission Manifest"
    data = requests.get(mission_url).json()
    sol_url = data['sols'][455]['url']

    print "Fetching Data"
    data = requests.get(sol_url).json()
    images = data["fcam_images"]

    print "Downloading %d images" % (len(images)) 
    for img in images:
        print img
        download_file(img["images"][-1]["url"])

    print "Enjoy!"

def download_file(url):
    print "Downloading file:\n" + url 
    local_filename = "img/" + url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

nasa()
