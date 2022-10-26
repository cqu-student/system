import React from 'react';
import { Link } from 'react-router-dom';
import "./Home.css";
function Home(){
    return (
        <div className='homepage' style={{backgroundImage:"url("+require("./background.jpg")+")"}}>
            <div className="right_div">
                <div className='Title'><p className='title'>基于场景理解的图片分割与识别系统</p></div>
                <div className='choose'>
                    <h2>账号登录</h2>
                    <form>
                        <div className='inputbox'>
                            <input type="text" name='' required=""></input>
                            <label>账号</label>
                        </div>
                        <div className='inputbox'>
                            <input type="password" name=" " required=""></input>
                            <label>密码</label>
                        </div>
                        <div className='choosebox'>
                            <input type="submit" name="regist" value="登录"></input>
                            <button type='regist'><Link className='regist_link' to="/login" >注册</Link></button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Home;