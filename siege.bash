siege -c 100 -d1 -t 30S 'http://localhost:80/ POST content=Lorem%20ipsum%20dolor%20sit%20amet,%20consectetur%20adipiscing%20elit,%20sed%20do%20eiusmod%20tempor%20incididunt%20ut%20labore%20et%20dolore%20magna%20aliqua.%20Ut%20enim%20ad%20minim%20veniam,%20quis%20nostrud%20exercitation%20ullamco%20laboris%20nisi%20ut%20aliquip%20ex%20ea%20commodo%20consequat.%20Duis%20aute%20irure%20dolor%20in%20reprehenderit%20in%20voluptate%20velit%20esse%20cillum%20dolore%20eu%20fugiat%20nulla%20pariatur.%20Excepteur%20sint%20occaecat%20cupidatat%20non%20proident,%20sunt%20in%20culpa%20qui%20officia%20deserunt%20mollit%20anim%20id%20est%20laborum.'
curl -X POST http://localhost/delete-all