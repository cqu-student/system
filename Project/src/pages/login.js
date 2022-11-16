import React, {useEffect,useState } from 'react';
import "./login.css";
import { Link } from 'react-router-dom';
import axios from 'axios';
function Login(){
    const [account, setAccount] = useState();
    const [password, setPassword] = useState();
    const [email,setEmail] = useState();
    const [telephone,setTelephone] = useState();
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
                setList(res.data)
                setUserLIST(null)
            })
                .catch(err => {
                    console.error(err);
                })
        }
    }, [init])
    const handleLogin = (e) => {
        e.preventDefault();
        //判断输入账号和密码
        console.log("userlist", uesrlist);
        let number = String(list.length+1);
        let data = new FormData()
        data.append('id',number)
        data.append('useraccount',account)
        data.append('userpassword',password)
        data.append('useremail',email)
        data.append('usertelephone',telephone)
        if (uesrlist === null) {
            let temp = {};
            for (let i = 0; i < list.length; i++) {
                temp[list[i][1]] = list[i][2];
            }
            setUserLIST(temp);
            if(temp[account]!==undefined)
            {
                alert("已注册账号该账号");
            }
            else{
                console.log(number)

                let api1 = urls + '/add/'
                axios({
                    method: 'post',
                    url: api1,
                    data:data,
                    timeout:1000,
                    headers:{'Content-Type':'multipart/form-data'}
                })
                .then(function(response){
                    alert("注册成功")
                    console.log(response);
                })
                .catch(function(error){
                    alert("注册失败,请联系技术人员")
                    console.log(error);
                })
            }
        }
        else{
            if(uesrlist[account]!==undefined)
            {
                alert("已注册账号该账号");
            }
            else{
                let api1 = urls + '/add/'
                axios({
                    method: 'post',
                    url: api1,
                    data:data,
                    timeout:1000,
                    headers:{'Content-Type':'multipart/form-data'}
                })
                .then(function(response){
                    console.log(response);
                    alert("注册成功")
                })
                .catch(function(error){
                    console.log(error);
                    alert("注册失败,请联系技术人员")
                })
            }
            
        }
    }
    return (
        <div className='homepage' style={{backgroundImage:"url("+require("./background.jpg")+")"}}>
            <div className="right_div">
                <div className='Title'><p className='title'>基于场景理解的图片分割与识别系统</p></div>
                <div className='choose_1'>
                    <h2>账号注册</h2>
                    <form onSubmit={handleLogin}>
                        <div className='inputbox'>
                            <input type="text" name='user' required="" onChange={e=> setAccount(e.target.value)}></input>
                            <label>账号</label>
                        </div>
                        <div className='inputbox'>
                            <input type="text" name="pwd" required="" onChange={e=>setPassword(e.target.value)}></input>
                            <label>密码</label>
                        </div>
                        <div className='inputbox'>
                            <input type="text" name='account' required="" onChange={e=>setEmail(e.target.value)}></input>
                            <label>邮箱</label>
                        </div>
                        <div className='inputbox'>
                            <input type="text" name='telephone' required="" onChange={e=>setTelephone(e.target.value)}></input>
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

export default Login;