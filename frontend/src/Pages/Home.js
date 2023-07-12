import styled from "styled-components";
import iconn from "../Images/icon.png";
import {Link} from "react-router-dom";
import Header from "../Components/Header"
import Footer from "../Components/Footer";
import Intro from "../Components/Intro";
const Container = styled.div`
    display: flex;
    flex-direction: column;
    margin-top: 10vh;
 
    .general{

        section.sec1{
        background-color: #FF8A00;
        margin: 0;
        padding: 20px 0px 50px 0px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;

        
        div.first{
            background-color: #FF8A00;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #fff;

            h1{
                font-size: 55px;
                font-weight: 500;
                margin-bottom: 5px;
            }

            h2{
                margin: 0px;
                font-weight: lighter;
            }
        
            a{
                margin-top: 04%;
                text-decoration: none;
            }
            button{
                    font-size: 16px!important;
                    width: 180px;
                    height: 60px;
                    background: #001935;
                    cursor: pointer;
                    border: none!important;
                    border-radius: 10px;
                    /* margin-top: 10px; */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #fff;
                    margin-top: 04%;
                }
                
                button:hover{
                        color: #0a58ca;
                    }

                
            }
    }

    section.sec2{
        background-color: #F8F9FA;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 50px 0px 60px 0px;

            h2{
                color: #001935;
                font-size: 48px;
                margin-bottom: 0px;
            }
            span{
                margin-top: 0px;
                font-size: 18px;
                color: #98a1ad;
                font-weight: 600px;
            }

        div.second{
                height: 50vh;
                display: flex;
                align-items: center;
                flex-direction: row;
                gap: 50px;

                div.content{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 30vh;
                    width: 50vh;
                    border: 1px solid black;
                    color: #001935; 
                    margin-top: 0px;
                    padding: 0px;
                    border: none;
                    border-radius: 12px;

                    box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -webkit-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -moz-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);

                    .logo{
                        border: none;
                        height: 80px;
                        width: 80px;
                        border-radius: 50%;
                        background-color: #FFF1E4;
                    }

                }

                .content:hover{
                            animation: vibrate 1.5s linear both;
                            @keyframes vibrate {
                            0% {
                                transform: translate(0);
                            }
                            20% {
                                transform: translate(-2px, 2px);
                            }
                            40% {
                                transform: translate(-2px, -2px);
                            }
                            60% {
                                transform: translate(2px, 2px);
                            }
                            80% {
                                transform: translate(2px, -2px);
                            }
                            100% {
                                transform: translate(0);
                        }
                        }   
                    }

                    h3{
                        margin: 0px;
                        font-size: 27px;
                        /* margin-top: 22px; */
                    }
                }
          
    }  
    }
    

    @media (max-width: 1115px) and (min-width: 768px){
        display: flex;
        flex-direction: column;
        margin-top: 10%;
        .general{
       section.sec1{
        background-color: #FF8A00;
        margin: 0;
        padding: 20px 0px 20px 0px;
        display: flex;
        flex-direction: column;
        position: relative;

        
        div.first{
            background-color: #FF8A00;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #fff;
            /* border: 1px solid; */

            h1{
                font-size: 45px;
                font-weight: 500;
                margin-bottom: 5px;
                /* border: 1px solid; */
            }

            h2{
                font-weight: lighter;
                /* border: 1px solid; */
                text-align: center;
            }
            .pot{
                display: none;
            }
            .top::after{
                content: " to complete everything on time and acheive you goals";
            }
        
            a{
                margin-top: 04%;
                text-decoration: none;
            }
            button{
                    font-size: 16px!important;
                    width: 180px;
                    height: 60px;
                    background: #001935;
                    cursor: pointer;
                    border: none!important;
                    border-radius: 10px;
                    /* margin-top: 10px; */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #fff;
                    margin-top: 04%;
                }
                
                button:hover{
                        color: #0a58ca;
                    }

                
            }
    }

    section.sec2{
        background-color: #F8F9FA;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: auto;
        /* border: 1px solid red; */
        padding: 0px;

            h2{
                color: #001935;
                font-size: 45px;
                margin-bottom: 0px;
            }
            span{
                margin-top: 0px;
                font-size: 18px;
                color: #98a1ad;
                font-weight: 600px;
            }

        div.second{
                height: auto;
                display: grid;
                gap: 50px;
                /* border: 1px solid black; */
                margin: 10px;

                div.content{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 30vh;
                    width: 65vw;
                    /* border: 1px solid black; */
                    color: #001935; 
                    margin-top: 0px;
                    padding: 0px;
                    border: none;
                    border-radius: 12px;
                    gap: 10px;

                    box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -webkit-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -moz-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);

                    .logo{
                        border: none;
                        height: 80px;
                        width: 80px;
                        border-radius: 50%;
                        background-color: #FFF1E4;
                    }

                }

                .content:hover{
                            animation: vibrate 1.5s linear both;
                            @keyframes vibrate {
                            0% {
                                transform: translate(0);
                            }
                            20% {
                                transform: translate(-2px, 2px);
                            }
                            40% {
                                transform: translate(-2px, -2px);
                            }
                            60% {
                                transform: translate(2px, 2px);
                            }
                            80% {
                                transform: translate(2px, -2px);
                            }
                            100% {
                                transform: translate(0);
                        }
                        }   
                    }

                    h3{
                        margin: 0px;
                        font-size: 27px;
                        /* margin-top: 22px; */
                    }
                }
          
            }  
            }
            
    }

    @media (max-width: 766px) and (min-width: 365px){
        display: flex;
        flex-direction: column;
        margin-top: 14%;
        
        .general{
       section.sec1{
        background-color: #FF8A00;
        margin: 0;
        padding: 20px 0px 20px 0px;
        display: flex;
        flex-direction: column;
        position: relative;

        
        div.first{
            background-color: #FF8A00;
            padding: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #fff;
            /* border: 1px solid; */

            h1{
                font-size: 35px;
                font-weight: 600;
                margin-bottom: 5px;

                /* border: 1px solid; */
            }

            h2{
                font-weight: lighter;
                /* border: 1px solid; */
                text-align: center;
                font-size: 22px;
            }
            .pot{
                display: none;
            }
            .top::after{
                content: " to complete everything on time and acheive you goals";
            }
        
            a{
                margin-top: 04%;
                text-decoration: none;
            }
            button{
                    font-size: 16px!important;
                    width: 180px;
                    height: 60px;
                    background: #001935;
                    cursor: pointer;
                    border: none!important;
                    border-radius: 10px;
                    /* margin-top: 10px; */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #fff;
                    margin-top: 04%;
                }
                
                button:hover{
                        color: #0a58ca;
                    }

                
            }
    }

    section.sec2{
        background-color: #F8F9FA;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: auto;
        /* border: 1px solid red; */
        padding: 0px;

            h2{
                color: #001935;
                font-size: 45px;
                margin-bottom: 0px;
            }
            span{
                margin-top: 0px;
                font-size: 18px;
                color: #98a1ad;
                font-weight: 600px;
            }

        div.second{
                height: auto;
                display: grid;
                gap: 50px;
                /* border: 1px solid black; */
                margin: 10px;

                div.content{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 30vh;
                    width: 70vw;
                    /* border: 1px solid black; */
                    color: #001935; 
                    margin-top: 0px;
                    padding: 0px;
                    border: none;
                    border-radius: 12px;
                    gap: 5px;
                    padding: 20px;

                    box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -webkit-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -moz-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);

                    .logo{
                        border: none;
                        height: 80px;
                        width: 80px;
                        border-radius: 50%;
                        background-color: #FFF1E4;
                    }

                }

                .content:hover{
                            animation: vibrate 1.5s linear both;
                            @keyframes vibrate {
                            0% {
                                transform: translate(0);
                            }
                            20% {
                                transform: translate(-2px, 2px);
                            }
                            40% {
                                transform: translate(-2px, -2px);
                            }
                            60% {
                                transform: translate(2px, 2px);
                            }
                            80% {
                                transform: translate(2px, -2px);
                            }
                            100% {
                                transform: translate(0);
                        }
                        }   
                    }

                    h3{
                        margin: 0px;
                        font-size: 27px;
                        /* margin-top: 22px; */
                    }
                }
          
            }  
            }
            
    }
    @media (max-width: 364px) and (min-width: 100px){
        display: flex;
        flex-direction: column;
        margin-top: 16%;
        
        .general{
       section.sec1{
        background-color: #FF8A00;
        margin: 0;
        padding: 20px 0px 20px 0px;
        display: flex;
        flex-direction: column;
        position: relative;

        
        div.first{
            background-color: #FF8A00;
            padding: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #fff;
            /* border: 1px solid; */

            h1{
                font-size: 30px;
                font-weight: 600;
                margin-bottom: 5px;

                /* border: 1px solid; */
            }

            h2{
                font-weight: lighter;
                /* border: 1px solid; */
                text-align: center;
                font-size: 20px;
            }
            .pot{
                display: none;
            }
            .top::after{
                content: " to complete everything on time and acheive you goals";
            }
        
            a{
                margin-top: 04%;
                text-decoration: none;
            }
            button{
                    font-size: 16px!important;
                    width: 180px;
                    height: 60px;
                    background: #001935;
                    cursor: pointer;
                    border: none!important;
                    border-radius: 10px;
                    /* margin-top: 10px; */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #fff;
                    margin-top: 04%;
                }
                
                button:hover{
                        color: #0a58ca;
                    }

                
            }
    }

    section.sec2{
        background-color: #F8F9FA;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: auto;
        /* border: 1px solid red; */
        padding: 0px;

            h2{
                color: #001935;
                font-size: 45px;
                margin-bottom: 0px;
            }
            span{
                margin-top: 0px;
                font-size: 18px;
                color: #98a1ad;
                font-weight: 600px;
            }

        div.second{
                height: auto;
                display: grid;
                gap: 50px;
                /* border: 1px solid black; */
                margin: 10px;

                div.content{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 30vh;
                    width: 70vw;
                    /* border: 1px solid black; */
                    color: #001935; 
                    margin-top: 0px;
                    padding: 0px;
                    border: none;
                    border-radius: 12px;
                    gap: 5px;
                    padding: 20px;

                    box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -webkit-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);
                    -moz-box-shadow: 1px 1px 9px -6px rgba(0,0,0,1);

                    .logo{
                        border: none;
                        height: 80px;
                        width: 80px;
                        border-radius: 50%;
                        background-color: #FFF1E4;
                    }

                }

                .content:hover{
                            animation: vibrate 1.5s linear both;
                            @keyframes vibrate {
                            0% {
                                transform: translate(0);
                            }
                            20% {
                                transform: translate(-2px, 2px);
                            }
                            40% {
                                transform: translate(-2px, -2px);
                            }
                            60% {
                                transform: translate(2px, 2px);
                            }
                            80% {
                                transform: translate(2px, -2px);
                            }
                            100% {
                                transform: translate(0);
                        }
                        }   
                    }

                    h3{
                        margin: 0px;
                        font-size: 27px;
                        /* margin-top: 22px; */
                    }
                }
          
            }  
            }
            
    }

`;

const Home = () => {
    return ( 
        <Container>

            <Header></Header>
                <Intro></Intro>
            <div className="general">
              <section className="sec1">
                <div className="first">
                    <h1>Be Ahead of your Peers</h1>

                    <h2 className="top">
                        A superior method to work awaits. Pro Manager helps you to take control of your projects and teams that will help you
                    </h2>
                    <h2 className="pot">
                    to complete everything on time and achieve your goals.
                    </h2>

                   <Link to="/register"><button>Try Now</button></Link> 
                </div>
            </section>

            <section className="sec2">
                     <h2>How It Works?</h2>
                     <span>Tool for anyone, anywhere</span>

                <div className="second">
                    
                <div className="content">
                        <div className="logo"></div>
                        <h3>Access Unlimited </ h3>
                       <h3 > Projects</h3>
                    </div>

                    <div className="content">
                        <div className="logo"></div>
                        <h3>Stay organized and </ h3>
                       <h3 > connected</h3>
                    </div>

                    <div className="content">
                        <div className="logo"></div>
                        <h3>Invite Your </ h3>
                       <h3 > Team mates</h3>
                    </div>

                </div>
            </section>  
            </div>
            

            <Footer></Footer>

        </Container>
     );
}
 
export default Home;