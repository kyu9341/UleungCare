package com.example.uleungcare;

import android.os.AsyncTask;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;

import static java.sql.DriverManager.println;

public class ControllerActivity extends AppCompatActivity {

    private int tvOnOff = 2; // TV 상태 ( 켜짐 : 1, 꺼짐 : 0)
    private int airconOnOff = 2; //  에어컨 상태 ( 켜짐 : 1, 꺼짐 : 0)
    private int airconTempUpDown = 0; // 에어컨 온도 up down
    private int tvChUpDown = 0; // TV 채널 up down
    private int tvVolUpDown = 0; //TV 볼륨 up down


    Button tvonButton;
    Button airconOnButton;
    Button airUpButton;
    Button airDownButton;
    Button tvVolUp;
    Button tvChUp;
    Button tvVolDown;
    Button tvChDown;


    private AlertDialog dialog; // 알림창


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_controller);

        tvonButton = (Button)findViewById(R.id.tvonButton);
        airconOnButton = (Button)findViewById(R.id.airconOnButton);
        airUpButton = (Button)findViewById(R.id.airUpButton);
        airDownButton = (Button)findViewById(R.id.airDownButton);
        tvVolUp = (Button)findViewById(R.id.tvVolUp);
        tvChUp = (Button)findViewById(R.id.tvChUp);
        tvVolDown = (Button)findViewById(R.id.tvVolDown);
        tvChDown = (Button)findViewById(R.id.tvChDown);


        tvonButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if(tvOnOff != 1){ // 초기 설정값인 2 이거나 꺼짐 상태인 0 인경우
                    tvOnOff = 1;
                }else{ // tv가 켜진경우
                    tvOnOff = 0;
                }
                sendRequest();
            }
        });

        airconOnButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(airconOnOff != 1){ // 초기 설정값인 2 이거나 꺼짐 상태인 0 인경우
                    airconOnOff = 1;
                }else{ // 에어컨이 켜진경우
                    airconOnOff = 0;
                }
                sendRequest();
            }
        });











        if(AppHelper.requestQueue == null){
            //리퀘스트큐 생성 (MainActivit가 메모리에서 만들어질 때 같이 생성이 될것이다.
            AppHelper.requestQueue = Volley.newRequestQueue(getApplicationContext());
        }


    }

    public void sendRequest(){
        String url = "http://10.0.2.2:8000/uleung/AndroidControl/";

        //StringRequest를 만듬 (파라미터구분을 쉽게하기위해 엔터를 쳐서 구분하면 좋다)
        //StringRequest는 요청객체중 하나이며 가장 많이 쓰인다고한다.
        //요청객체는 다음고 같이 보내는방식(GET,POST), URL, 응답성공리스너, 응답실패리스너 이렇게 4개의 파라미터를 전달할 수 있다.(리퀘스트큐에 )
        //화면에 결과를 표시할때 핸들러를 사용하지 않아도되는 장점이있다.
        StringRequest request = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {  //응답을 문자열로 받아서 여기다 넣어달란말임(응답을 성공적으로 받았을 떄 이메소드가 자동으로 호출됨
                    @Override
                    public void onResponse(String response) {
                        Log.e("응답 => "+ response, "응답 => ");

                        try {
                            JSONObject jsonResponse = new JSONObject(response);
                            boolean success = jsonResponse.getBoolean("success");
                            if (success) {
                                AlertDialog.Builder builder = new AlertDialog.Builder(ControllerActivity.this);
                                dialog = builder.setMessage("전송 성공.")
                                        .setPositiveButton("확인", null)
                                        .create();
                                dialog.show();
                            } else {
                                AlertDialog.Builder builder = new AlertDialog.Builder(ControllerActivity.this);
                                dialog = builder.setMessage("전송 실패.")
                                        .setNegativeButton("확인", null)
                                        .create();
                                dialog.show();
                            }

                        } catch (Exception e) {
                            e.printStackTrace();
                        }

                    }
                },
                new Response.ErrorListener(){ //에러발생시 호출될 리스너 객체
                    @Override
                    public void onErrorResponse(VolleyError error) {

                        Log.e("에러 => "+ error.getMessage(), "에러 => ");
                    }
                }
        ){
            //만약 POST 방식에서 전달할 요청 파라미터가 있다면 getParams 메소드에서 반환하는 HashMap 객체에 넣어줍니다.
            //이렇게 만든 요청 객체는 요청 큐에 넣어주는 것만 해주면 됩니다.
            //POST방식으로 안할거면 없어도 되는거같다.
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> params = new HashMap<String, String>();

                params.put("tvOnOff", tvOnOff+"");
                params.put("airconOnOff", airconOnOff+"");
                params.put("airconTempUpDown", airconTempUpDown+"");
                params.put("tvChUpDown", tvChUpDown+"");
                params.put("tvVolUpDown", tvVolUpDown+"");


                return params;


            }

/*
            @Override
            public Map<String, String> getHeaders() throws AuthFailureError {
                HashMap<String, String> headers = new HashMap<String, String>();
                headers.put("Content-Type", "application/json; charset=utf-8");
                return headers;
            }
            */
        };

        //아래 add코드처럼 넣어줄때 Volley라고하는게 내부에서 캐싱을 해준다, 즉, 한번 보내고 받은 응답결과가 있으면
        //그 다음에 보냈을 떄 이전 게 있으면 그냥 이전거를 보여줄수도  있다.
        //따라서 이렇게 하지말고 매번 받은 결과를 그대로 보여주기 위해 다음과같이 setShouldCache를 false로한다.
        //결과적으로 이전 결과가 있어도 새로 요청한 응답을 보여줌
        request.setShouldCache(false);
        AppHelper.requestQueue.add(request);

    }

}
