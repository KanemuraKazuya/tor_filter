import re
import requests


if __name__ == '__main__':
  # tor exit nodes
  url = 'https://check.torproject.org/exit-addresses'
  pattern = r"ExitAddress.*"

  node_line = re.compile(pattern)
  
  src = requests.get(url).text
  
  exit_nodes = node_line.findall(src)

  f = open("/etc/nginx/conf.d/deny-tor.conf", "w")

  for line in exit_nodes:
    f.writelines("deny " + line.split(" ")[1] + "/32;\n")


  

   
