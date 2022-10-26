import axios from 'axios'
import {message} from 'antd'
export default function ajax{URL, data = {}, type = 'GET'}{
    return new Promise((resolve,reject)=>{
        let Promise
        if(type === 'GET'){//发送GET请求
            Promise = axios.get((url,{//配置对象
                params: data //指定请求参数
            }))
        } else { //发POST请求
            Promise = axios.post(url,data)
        }
        //如果成功了，则调用resolve(value)
        Promise.then(resolve=>{
            resolve(response.data)
        //3.如果失败了,不调用reject(reason),而是提示异常信息
        }).catch(error => {
            message.error('请求出错了:'+error.message)
        })
    })
}