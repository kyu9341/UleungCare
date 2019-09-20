package com.example.uleungcare;

import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

public class ControllerActivity extends AppCompatActivity {

    private int tvOnOff = 0; // TV 상태 ( 켜짐 : 1, 꺼짐 : 0)
    private int airconOnOff = 0; //  에어컨 상태 ( 켜짐 : 1, 꺼짐 : 0)
    private int airconTempUp = 0; // 에어컨 온도 up Count
    private int airconTempDown = 0; // 에어컨 온도 down Count

    Button tvonButton;
    Button airconOnButton;
    Button airUpButton;
    Button airDownButton;

    private AlertDialog dialog; // 알림창


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_controller);

        tvonButton = (Button)findViewById(R.id.tvonButton);
        airconOnButton = (Button)findViewById(R.id.airconOnButton);
        airUpButton = (Button)findViewById(R.id.airUpButton);
        airDownButton = (Button)findViewById(R.id.airDownButton);

        tvonButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(tvOnOff == 0){
                    tvOnOff = 1;
                }else{
                    tvOnOff = 0;
                }
            }


            Response.Listener<String> responseListener = new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    try
                    {

                        JSONObject jsonResponse = new JSONObject(response);
                        boolean success = jsonResponse.getBoolean("success");
                        if(success) {
                            AlertDialog.Builder builder = new AlertDialog.Builder(ControllerActivity.this);
                            dialog = builder.setMessage("전송 성공.")
                                    .setPositiveButton("확인", null)
                                    .create();
                            dialog.show();
                        }else{
                            AlertDialog.Builder builder = new AlertDialog.Builder(ControllerActivity.this);
                            dialog = builder.setMessage("전송 실패.")
                                    .setNegativeButton("확인", null)
                                    .create();
                            dialog.show();
                        }

                    }

                    catch (Exception e){
                        e.printStackTrace();
                    }
                    ControllerRequest controllerRequest = new ControllerRequest(tvOnOff, airconOnOff, airconTempUp, airconTempDown, responseListener);
                    RequestQueue queue = Volley.newRequestQueue(ControllerActivity.this);
                    queue.add(controllerRequest);
                }
            };



        });


    }
}
