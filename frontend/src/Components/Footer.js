import {Link} from "react-router-dom";
import styled from "styled-components";


const Container = styled.div`
        display: flex;
        flex-direction: column;
            div.footer{
        background-color: #FFF1E4;
        display: flex;
        padding: 47px 80px;
        gap: 35%;

        
        div{
            /* border: 1px solid; */
            display: flex;
            padding: 0px;

            h2{ 

                color: #ff8a00;
                font-size: 24px;
                margin-bottom: 0px;
                font-weight: 600;
                opacity: 90%;
                outline: none;
            }
            

            a{
                text-decoration: none;
            }
            li{
                list-style: none;
                color: #001935;
                    font-size: 15px;
                    margin: 10px 0px;
                    display: block;
                    font-weight: 600;
                    
                }
            }

    }

    div.bottom{
        background-color: #001935;
        color: #fff;
        
        h4{
            font-weight: 400;
            text-align: center;
        }
    };
       
`


const Footer = () => {
    return ( 
        <Container>
                <div className="footer">
        <div>
            <ul>
                <h2>Quick Links</h2>
                <Link><li>About Us</li></Link>
                <Link><li>Help/FAQ</li></Link>
            </ul>
        </div>
        <div>
            <ul>
                <h2>Legal Info</h2>
                <Link to="/"><li>Privacy Center</li></Link>
                <Link to="/"><li>Cookies</li></Link>
                <Link to="/"><li>Privacy</li></Link>
                <Link to="/"> <li>Terms</li></Link>
            </ul>
        </div>
        
    </div>

    <div className="bottom">
        <h4> © Copyright 2023 Project Manager | All Rights Reserved</h4>
    </div>

        </Container>
        
     );
}
 
export default Footer;