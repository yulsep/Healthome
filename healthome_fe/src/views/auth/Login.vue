<template>
    <main class="wrapper-login">
        <div class="wrapper-form">
            <form class="form-login">
            <div>
                <h2>Welcome Back</h2>
                <h3>Enter your email and password to Log In</h3>
            </div>
            <div class="input-login">
                <label>Email <input type="email" name="email"></label>
                <label>Password <input type="password" name="password"></label>
            </div>
            <button>Log In</button>  
            </form>
        </div>
        
        <div class="wrapper-logo">
            <picture>
                <img src="@/assets/logo2.png" alt="logo">
            </picture>
        </div>
    </main>

</template>
<script>
export default {
    
}
</script>
<style lang="css">
    .wrapper-login{
        display: grid;
        grid-template-columns: 1fr 1fr;
        height: 950px;
    }

    .wrapper-logo{
        width: 100%;
        max-width: 900px;
        min-width: 300px;
    }

    .wrapper-logo picture{
        display: flex;
        height: 100%;
        align-items: center;
        justify-content: center;
        background-color: #A8CDFF;
        border-radius: 0px 0px 0px 40px;
        margin-top: -60px;
    }

    .wrapper-form {
        display: flex;
        align-items: center;
        padding: 0 3rem;
        justify-content: center;
    }

    .form-login{
        display: grid;
        gap: 3rem;
    }

    h2{
        font: normal normal bold 50px/80px Roboto;
        letter-spacing: 0px;
        color: #1D517E;
        opacity: 1;
        height: 3%;
    }

    h3{
        font: normal normal bold 18px/80px Roboto;
        letter-spacing: 0px;
        color: #928F8F;
        opacity: 1;
    }

    button{
        background: #1D517E 0% 0% no-repeat padding-box;
        box-shadow: 0px 3px 6px #00000029;
        border-radius: 12px 0px 12px 12px;
        opacity: 1;
        display: grid;
        align-content: center;
        
        width: 100%;
        height: 50%;
        text-align: center;
        font: normal normal normal 22px/80px Roboto;
        letter-spacing: 0px;
        color: #FFFFFF;
        opacity: 1;

    }

    .input-login{
        display: grid;
        grid-template-columns: min-content;
        font: normal normal bold 20px Roboto;
        letter-spacing: 0px;
        color: #928F8F;
    }

    input{
        background: #FFFFFF 0% 0% no-repeat padding-box;
        border: 1px solid #BFBFBF;
        border-radius: 12px;
        opacity: 1;
        width: 329.45px;
        height: 35px;
        display: flex;
        align-self: center;
    }

</style>