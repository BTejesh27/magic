<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<meta name="viewport" content="width=device-width, user-scalable=no" />

<title>I-Regulon</title>
  <link href="font-awesome-4.7.0/css/font-awesome.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="bootstrap-3.3.7-dist/css/bootstrap.min.css">
  <link href="style.css" rel="stylesheet">
  <link rel="shortcut icon" type="image/png" href="icon.png">
</head>
<body>

  <div id="cy"></div>
  <div id="loading">
    <h4>...Loading....</h4>
    <span class="fa fa-spinner fa-spin" style='color:#000000;'></span>

  </div>

  <div id="search-wrapper">
    <span>
    <div style='font-size:32px;color:green;font-weight:bold;'>MAGICALDB</div>
    <div style='font-size:10px;'><img src='images/blue.png'>Gene <img src='images/red.png'>miRNA <img src='images/green.png'>Transcription Factor</div>
    
    Enter Gene</span> 
    <input type="text" class="form-control" id="search" placeholder="&#xf002; Search">
  </div>

  <div id="info">
  </div>


  <script src="fastclick.min.js"></script>
  <script src="jquery.min.js"></script>

  <script src="cytoscape.min.js"></script>

  <script src="jquery.qtip.min.js"></script>
  <link href="jquery.qtip.min.css" rel="stylesheet" type="text/css" />
  <script src="cytoscape-qtip.js"></script>

  <script src="bluebird.min.js"></script>
  <script src="bootstrap.min.js"></script>
  <script src="typeahead.bundle.js"></script>
  <script src="handlebars.min.js"></script>
  <script src="lodash.min.js"></script>

  <script src="demo.js"></script>


  <button id="about" class="btn btn-default"><i class="fa fa-info"></i></button>

  <div id="about-content">
    <p>This app was made using <a target="_blank" href="http://js.cytoscape.org">Cytoscape.js <i class="fa fa-external-link"></i></a>.</p>
  </div>

  
  <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-155159-12', 'auto');
    ga('send', 'pageview');

  </script>

</body>
</html>
