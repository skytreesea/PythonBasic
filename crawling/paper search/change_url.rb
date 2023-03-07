require 'cgi'

def change_url(name)
return CGI.escape name
end

change_url("김창현")
