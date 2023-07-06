import styled from "styled-components";
import { Link } from "react-router-dom";


const Container = styled.div`
        .intro{
            display: flex;
            gap: 20px;
            /* margin-left: 10%; */
            padding-left: 10%;
            background-color: #F8F9FA;
            top: 0px;
            position: absolute;
            width: 90%;

            a{
                text-decoration: none;
                color: #001935;
            }

            a:visited{
                
            }



                
            h3{
                font-size: 17px;
                /* font-family: sans-serif; */
                cursor: pointer;
                /* font-weight: 500; */
                opacity: 70%;
               
            }
            h3:hover{
                color: #FF8A00;
            }

        }

`
const Intro = () => {
    return ( 
        <Container>
            
            <div className="intro">
                    <Link><h3>About us</h3></Link>
                    <Link><h3>Help/FAQ</h3></Link>
                    
                </div>
                
        </Container>
     );
}
 
export default Intro;