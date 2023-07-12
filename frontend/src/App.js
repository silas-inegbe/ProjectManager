import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./Pages/Home";
import Login from "./Pages/Login";
import Register from "./Pages/Register";
import About from "./Pages/About";
const App = () => {
  return ( 
    <>
      <Router>
        <Routes>
          <Route path= "/" element={ <Home />} />
          <Route path= "/login" element={ <Login />} />
          <Route path= "/register" element={ <Register />} />
          <Route path= "/about" element={ <About />} />

        </Routes>
      </Router>
    
    </>
   );
}
 
export default App;
