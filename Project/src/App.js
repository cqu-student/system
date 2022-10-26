import React from "react";
import {
  BrowserRouter,
  Routes, 
  Route,
} from "react-router-dom";
import Home from './pages/Home';
import Login from  './pages/login';
import user1 from './pages/User1';
import user2 from './pages/User2';
function App(){
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login/>}/>
        <Route path="/user1" element={user1}/>
        <Route path="/user2" element={user2}/>
        <Route path="/" element={<Home/>}/>
      </Routes>
    </BrowserRouter>
  );
}
export default App;