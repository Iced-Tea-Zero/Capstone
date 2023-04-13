function showNewButton() {
    const newBtn = document.createElement('button');
    newBtn.textContent = 'New Button';
    
    newBtn.addEventListener('click', function() {
      this.remove(); // 클릭된 버튼을 삭제
    });
    
    document.getElementById('button-container').appendChild(newBtn);
  }
  
  document.getElementById('show-btn').addEventListener('click', showNewButton);
    


  const http = require('http');
  const fs = require('fs');
  
  const server = http.createServer((req, res) => {
    if (req.url === '/') {
      fs.readFile('index.html', (err, data) => {
        if (err) {
          res.writeHead(500, { 'Content-Type': 'text/html' });
          res.write('<h1>Error reading index.html file</h1>');
          res.end();
        } else {
          res.writeHead(200, { 'Content-Type': 'text/html' });
          res.write(data);
          res.end();
        }
      });
    } else if (req.url === '/click.css') {
      fs.readFile('click.css', (err, data) => {
        if (err) {
          res.writeHead(500, { 'Content-Type': 'text/css' });
          res.write('/* Error reading click.css file */');
          res.end();
        } else {
          res.writeHead(200, { 'Content-Type': 'text/css' });
          res.write(data);
          res.end();
        }
      });
    } else {
      res.writeHead(404, { 'Content-Type': 'text/html' });
      res.write('<h1>Page not found</h1>');
      res.end();
    }
  });
  
  server.listen(3000, () => {
    console.log('Server is running on port 3000');
  });
