#THCloud README
* Before running the website, ensure following programs are installed:
  + Nginx
  + Python Package Manager (pip)
  + Django
* To configure the website, run bootstrap script in folder NginxConfig.<br />
  (A folder containing certificates, keys and D-H params is needed in the process.<br />
  You can obtain the folder from local or by SSH)<br />
* To run the website, use "./manage.py runserver".<br />
  To run it in the background, use "nohup ./manage.py runserver >/dev/null 2>&1 &".<br />
  To kill the background website process, use "pkill python".<br />
