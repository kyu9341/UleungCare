package com.example.uleungcare;

import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class ControllerRequest extends StringRequest {
    final static private String URL = "http://20.0.2.2:8000/uleung/AndroidControl/";


    private Map<String, String> parameters;

    public ControllerRequest(int tvOnOff, int airconOnOff, int airconTempUp, int airconTempDown, Response.Listener<String> listener){
        super(Method.POST, URL, listener,null); // 해당 URL에 POST 방식으로 전송
        parameters = new HashMap<>(); // HashMap으로 초기화

        parameters.put("tvOnOff", tvOnOff+"");
        parameters.put("airconOnOff", airconOnOff+"");
        parameters.put("airconTempUp", airconTempUp+"");
        parameters.put("airconTempDown", airconTempDown+"");


    }


    @Override
    public Map<String, String> getParams(){
        return parameters;
    }
}


