import React from 'react';
import "./login.css";
import { Link } from 'react-router-dom';
function Home(){
    return (
        <div className='homepage' style={{backgroundImage:"url("+require("./background.jpg")+")"}}>
            <div className="right_div">
                <div className='Title'><p className='title'>基于场景理解的图片分割与识别系统</p></div>
                <div className='choose_1'>
                    <h2>账号注册</h2>
                    <form>
                        <div className='inputbox'>
                            <input type="text" name='user' required=""></input>
                            <label>账号</label>
                        </div>
                        <div className='inputbox'>
                            <input type="text" name="pwd" required=""></input>
                            <label>密码</label>
                        </div>
                        <div className='inputbox'>
                            <input type="text" name='account' required=""></input>
                            <label>身份证</label>
                        </div>
                        <div className='inputbox'>
                            <input type="text" name='telephone' required=""></input>
                            <label>电话号码</label>
                        </div>
                        <div className='choosebox'>
                            <input type="submit" name="regist" value="注册"></input>
                            <button type="return" name=''><Link className='regist_link' to="/" >返回登录</Link></button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Home;