package com.example.uleungcare;

import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class ControllerRequest extends StringRequest {
    final static private String URL = "http://127.0.0.1:8000/uleung/androidControl/";


    private Map<String, String> parameters;

    public ControllerRequest(String controlKey, int controlValue, Response.Listener<String> listener){
        super(Method.POST, URL, listener,null); // 해당 URL에 POST 방식으로 전송
        parameters = new HashMap<>(); // HashMap으로 초기화

        parameters.put(controlKey, controlValue+"");

    }


    @Override
    public Map<String, String> getParams(){
        return parameters;
    }
}


