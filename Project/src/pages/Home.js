import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import "./Home.css";
import axios from 'axios';
function Home(props) {
    const [account, setAccount] = useState();
    const [password, setPassword] = useState();
    const [list, setList] = useState();
    const [uesrlist, setUserLIST] = useState();
    const [urls] = useState('http://localhost:5000');
    const [init, setInit] = useState(false);
    useEffect(() => {
        setInit(true);
    }, [])

    useEffect(() => {
        if (init === true) {
            var api = urls + "/users/";
            axios.get(api).then(res => {
                console.log("res", res);
                console.log("res_data", res.data)
                setList(res.data)
                setUserLIST(null)
            })
                .catch(err => {
                    console.error(err);
                })
        }
    }, [init])
    const handleSubmit = (e) => {
        let url = '/user1'
        e.preventDefault();
        //判断输入账号和密码
        console.log("userlist", uesrlist);
        if (uesrlist === null) {
            let temp = {};
            for (let i = 0; i < list.length; i++) {
                temp[list[i][1]] = list[i][2];
            }
            setUserLIST(temp);
            if(temp[account]===undefined)
            {
                alert("未注册账号");
            }
            else if(temp[account] !== password)
            {
                alert("密码错误");
            }
            else{
                console.log(props.history);
                window.location.href = url
            }
        }
        else{
            if(uesrlist[account]===undefined)
            {
                alert("未注册账号");
            }
            else if(uesrlist[account] !== password)
            {
                alert("密码错误");
            }
            else{
                console.log(props.history);
                window.location.href = url
            }
        }
    }

    return (
        <div className='homepage' style={{ backgroundImage: "url(" + require("./background.jpg") + ")" }}>
            <div className="right_div">
                <div className='Title'><p className='title'>基于场景理解的图片分割与识别系统</p></div>
                <div className='choose'>
                    <h2>账号登录</h2>
                    <form onSubmit={handleSubmit}>
                        <div className='inputbox'>
                            <input type="text" name='' required="" onChange={e => setAccount(e.target.value)}></input>
                            <label>账号</label>
                        </div>
                        <div className='inputbox'>
                            <input type="password" name=" " required="" onChange={e => setPassword(e.target.value)}></input>
                            <label>密码</label>
                        </div>
                        <div className='choosebox'>
                            <input type="submit" name="regist" value="登录"></input>
                            <button type='button'><Link className='regist_link' to="/login" >注册</Link></button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Home;