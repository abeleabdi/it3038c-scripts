var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");


var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname();
        serverUptime=os.uptime();
        total_memory=os.totalmem();
        free_memory=os.freemem();
        cpus=os.cpus();
       
        html=`
        <!DOCTYPE html>
        <head>
             <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${serverUptime}</p>
            <p>Total Memory: ${total_memory}</p>
            <p>Free Memory: ${free_memory}</p>
            <p>Number of CPUs: ${cpus}</p>
        </body>
        </html> 
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);

    }
    else{
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Nott Found at ${req.url}`);
    }    

});

server.listen(3000);
console.log("Server listening on port 3000");
