import styled from "styled-components";
import { Link } from "react-router-dom";


const Container = styled.div`
    .general{
        .intro{
            display: flex;
            gap: 20px;
            /* margin-left: 10%; */
            padding-left: 10%;
            background-color: #F8F9FA;
            /* position: absolute; */
            align-items: center;
            width: auto;
            top: 500px;

            a{
                text-decoration: none;
                color: #001935;
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
    }
        @media (max-width: 1115px){
            .general{
                .intro{
            display: flex;
            gap: 50px;
            /* margin-left: 10%; */
            padding-left: 10%;
            background-color: #F8F9FA;
            top: 60px;
            width: 90%;
            height: auto;

            a{
                text-decoration: none;
                color: #001935;
            }

            a:visited{
                
            }



                
            h3{
                font-size: 15px;
                /* font-family: sans-serif; */
                cursor: pointer;
                /* font-weight: 500; */
                opacity: 70%;
               
            }
            h3:hover{
                color: #FF8A00;
            }

                }
            }
        }
    
        @media (max-width: 766px){
            .general{
                .intro{
            display: flex;
            gap: 50px;
            /* margin-left: 10%; */
            padding-left: 10%;
            background-color: #F8F9FA;
            width: 90%;
            margin-top: 20px;

            a{
                text-decoration: none;
                color: #001935;
            }

            a:visited{
                
            }



                
            h3{
                font-size: 15px;
                /* font-family: sans-serif; */
                cursor: pointer;
                /* font-weight: 500; */
                opacity: 70%;
               
            }
            h3:hover{
                color: #FF8A00;
            }

                }
            }
        }
    
    
`
const Intro = () => {
    return ( 
        <Container>
            <div className="general">
                <div className="intro">
                    <Link to="/about"><h3>About us</h3></Link>
                    <Link><h3>Help/FAQ</h3></Link>
                    
                </div>
            </div>    
        </Container>
     );
}
 
export default Intro;