<?php
include("conexao.php");
if(isset($_POST["email"]) && strlen($_POST["email"]) > 0){

	if(!isset($_SESSION))
		session_start();

	$_SESSION['email'] = $mysqli->escape_string($_POST['email']);
	$_SESSION['senha'] = md5(md5($_POST['senha']));

	$sql_code = "SELECT senha, IDusuario FROM usuario WHERE email = '$_SESSION[email]'";
	$sql_query = $mysqli->query($sql_code) or die ($mysqli->error);
	$dado = $sql_query->fetch_assoc();
	$total = $sql_query->num_rows;

	if($total == 0){
		$erro[] = "Este email não pertence à nenhum usuário.";
	}
	else{
		if ($dado['senha'] == $_SESSION['senha']){
			$_SESSION['usuario'] = $dado['codigo'];
		}
	else{
		$erro[] = "Senha incorreta.";
	}
	if(count($erro) == 0 ||  !isset($erro)){
		echo "<script>alert('Login efetuado com sucesso')location.href='sucesso.php';</script>";
	}
}
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Login</title>
	<link rel="icon" href="favicon.ico" type="image/x-icon" />    <meta charset="utf-8">
    <meta name="description" content="Urlist é uma plataforma virtual de organização, organize sua rotina conosco!">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="Organização, To-do List, Agenda">
    <meta name="author" content="Hannely Thays Maske, Jackson Ricardo Riebe, Maria Eduarda Leite.">
    <link rel="stylesheet" href="logincss.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
</head>
<body>
	<?php 
		if(count($erro) > 0)
		foreach($erro as $msg){
			echo "<p>$msg</p>";
		}
	?>
    <div class="container">
        <div class="content first-content">
            <div class="first-column">
                <h2 class="title title-primary">Bem-vindo de volta!</h2>
                <p class="description description-primary">Para se manter conectado conosco</p>
                <p class="description description-primary">por favor registre suas informações pessoais</p>
                <button id="signin" class="btn btn-primary">sign in</button>
            </div>    
            <div class="second-column">
                <h2 class="title title-second">criar conta</h2>
                <div class="social-media">
                    <ul class="list-social-media">
                        <a class="link-social-media" href="#">
                            <li class="item-social-media">
                                <i class="fab fa-facebook-f"></i>        
                            </li>
                        </a>
                        <a class="link-social-media" href="#">
                            <li class="item-social-media">
                                <i class="fab fa-google-plus-g"></i>
                            </li>
                        </a>
                        <a class="link-social-media" href="#">
                            <li class="item-social-media">
                                <i class="fab fa-linkedin-in"></i>
                            </li>
                        </a>
                    </ul>
                </div><!-- social media -->
                <p class="description description-second">ou registre-se com seu email:</p>
                <form action= "" method= "POST" class="form">
                    <label class="label-input" for="">
                        <i class="far fa-user icon-modify"></i>
                        <input type="text" required placeholder="Nome">
                    </label>
                    
                    <label class="label-input" for="">
                        <i class="far fa-envelope icon-modify"></i>
                        <input name= "email" type="email" required placeholder="Email">
                    </label>
                    
                    <label class="label-input" for="">
                        <i class="fas fa-lock icon-modify"></i>
                        <input name="senha" type="password" required placeholder="Senha">
                    </label>
                    
                    
                    <button class="btn btn-second">sign up</button>        
                </form>
            </div><!-- second column -->
        </div><!-- first content -->
        <div class="content second-content">
            <div class="first-column">
                <h2 class="title title-primary">Olá, amigo!</h2>
                <p class="description description-primary">Entre suas informações pessoais</p>
                <p class="description description-primary">e comece sua jornada conosco</p>
                <button id="signup" class="btn btn-primary">sign up</button>
            </div>
            <div class="second-column">
                <h2 class="title title-second">Login</h2>
                <div class="social-media">
                    <ul class="list-social-media">
                        <a class="link-social-media" href="#">
                            <li class="item-social-media">
                                <i class="fab fa-facebook-f"></i>
                            </li>
                        </a>
                        <a class="link-social-media" href="#">
                            <li class="item-social-media">
                                <i class="fab fa-google-plus-g"></i>
                            </li>
                        </a>
                        <a class="link-social-media" href="#">
                            <li class="item-social-media">
                                <i class="fab fa-linkedin-in"></i>
                            </li>
                        </a>
                    </ul>
                </div><!-- social media -->
                <p class="description description-second">ou entre com seu email:</p>
                <form action= "" method= "POST" class="form">
                
                    <label class="label-input" for="">
                        <i class="far fa-envelope icon-modify"></i>
                        <input value ="<?php echo $_SESSION['email']; ?>" type="email" required placeholder="Email">
                    </label>
                
                    <label class="label-input" for="">
                        <i class="fas fa-lock icon-modify"></i>
                        <input type="password" required placeholder="Senha">
                    </label>
                
                    <a class="password" href="esqueceuasenha.php">esqueceu sua senha?</a>
                    <button type="submit" class="btn btn-second">sign in</button>
                </form>
            </div><!-- second column -->
        </div><!-- second-content -->
    </div>
    <script src="jslogin.js"></script>
</body>
</html>