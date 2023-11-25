from typing import Optional
import io
import requests

def upload_to_catbox(file) -> Optional[str]:
	try:
		data = {
			'reqtype': (None, 'fileupload'),
        	'time': (None, '1h'),
			'userhash': (None, ''),
			'fileToUpload': file
		}
		r = requests.post("https://litterbox.catbox.moe/resources/internals/api.php", files=data)

		if not r.ok:
			print(r.text[:1000])

		return r.text
	except:
		print("An unexpected error occured while uploading image")
