import Header from "../Components/Header";
import Intro from "../Components/Intro";
import Footer from "../Components/Footer";
import styled from "styled-components";

const Container = styled.div`


    section.sec1{
        background-color: #FF8A00;
        margin: 0;
        padding: 80px 0px 90px 0px;
        display: flex;
        flex-direction: column;
        position: relative;
        height: 10vh;
        margin-bottom: 20px;

        
        div.first{
            background-color: #FF8A00;
            padding: 0px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #fff;
            height: 200%;

            h1{
                font-size: 55px;
                font-weight: 500;

            }

    }
}

    section.sec2{
        padding: 10px 15px ;
        background-color: #F8F9FA;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;

        div{
            font-size: 20px;
            width: 80%;
            /* border: 1px solid #FF8A00; */
            border-radius: 10px;
            padding-inline: 3%;
            padding-bottom: 4%;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.5);
            -webkit-box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.5);
            -moz-box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.5);

        }
        div.last{
            display: flex;
            flex-direction: column;

            span{
                width: 100%;
                /* border: 1px solid green; */
                height: 30px;
                
                            img{
                                border: 1px solid red;
                                height: 40%;
                            }
            }


        }

    }
`

const About = () => {
    return ( 
        <Container>
            <Header> </Header>

            <section className="sec1">
            <Intro></Intro>
            <div className="first">
                    <h1>About Us</h1>
            </div>
            </section>

            <section className="sec2">
                <div>
                    <h2>Who we are</h2>
                    <span>
                    <img src="" alt="" />
                    Welcome to our company, a leading provider of project management solutions for businesses and individuals. We are passionate about helping our clients streamline their project workflows, enhance collaboration, and achieve their project goals with ease.

                    <br /><br />At our company, we understand the challenges that organizations and individuals face when it comes to managing projects effectively. That's why we have developed a comprehensive project management app that empowers our clients to plan, execute, and track their projects efficiently, all in one place.

                    <br /><br />Our app offers a wide range of powerful features designed to simplify project management. From task management and scheduling to team collaboration and reporting, our app provides the tools you need to stay organized, meet deadlines, and deliver successful projects. Whether you are a small business, 
                    a growing startup, or an individual professional, our app is tailored to suit your specific needs.
                    </span>                
                </div>

                <div>
                    <h2>How it works</h2>
                    <ol>
                        <li>
                    Sign Up: Get started by signing up for our project management app. Create your account and provide the necessary information to set up your profile.
                        <br /></li>
                        <br /><li>
                    Create Projects: Once you're signed in, you can start creating projects. Give each project a name, set goals and objectives, and define timelines and milestones.
                        <br /></li>
                        <br /><li>
                    Add Tasks and Assignments: Break down your projects into manageable tasks. Assign tasks to team members, set priorities, and track progress. You can also add due dates and dependencies to ensure smooth workflow.
                        <br /></li>
                        <br /><li>
                    Collaborate and Communicate: Our app offers robust collaboration features. Invite team members to join your projects, share files, and engage in real-time discussions. Stay connected and aligned with your team, no matter where they are.
                        <br /></li>
                        <br /><li>
                    Track Progress: Monitor the progress of your projects with our intuitive project tracking tools. Get an overview of tasks completed, pending, and overdue. Stay informed about project status and make informed decisions.
                        <br /></li>
                        <br /><li>
                    Generate Reports: Our app provides powerful reporting capabilities. Generate insightful reports to track project performance, monitor team productivity, and analyze project data. Use these reports to measure success and identify areas for improvement.
                        <br /></li>
                        <br /><li>
                    Customize Workflows: Tailor the app to fit your unique workflow and preferences. Customize task categories, project templates, and notifications to match your specific requirements.
                        <br /></li>
                        <br /><li>
                    Access Anytime, Anywhere: Our project management app is cloud-based, allowing you to access your projects and data from anywhere, at any time. Stay productive whether you're in the office, working remotely, or on the go.
                        <br /></li>
                        <br /><li>

                    Integrate with Other Tools: Enhance your project management experience by integrating our app with other essential tools. Connect with popular apps like Slack, Trello, and Google Drive to streamline your workflow and maximize efficiency.
                        <br /></li>
                        <br /><li>

                    Dedicated Support: We pride ourselves on providing exceptional customer support. Our dedicated support team is here to assist you with any questions, concerns, or technical issues you may encounter along the way.
                            </li>
                </ol>
                </div>

                <div className="last">
                    <h2>Our Team</h2>
                    <span>
                        COMING SOON!!
                    </span>
                </div>
            </section>

            <Footer></Footer>
        </Container>
     );
}
 
export default About;