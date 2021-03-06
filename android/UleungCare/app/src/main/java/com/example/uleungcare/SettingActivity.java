package com.example.uleungcare;

import android.app.Dialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;


public class SettingActivity extends AppCompatActivity {

    Button redButton; // LED조명 색 지정
    Button greenButton;
    Button blueButton;
    private int ledThreshold = 3; // led가 켜지는 기준 조도
    private int airconThreshold = 0; // 에어컨이 켜지는 기준 온도
    private AlertDialog dialog; // 알림창
    Button IRregisterButton;

    EditText redValue; // 사용자 설정 rgb 값을 받을 text
    EditText greenValue;
    EditText blueValue;
    Button colorInsert; // 사용자 설정 color 입력
    TextView colorView; // color 확인
    private int r = 255, g = 255, b = 255; // rgb
    RadioGroup useGroup; // 에어컨 온도 설정 사용 or 사용x
    RadioGroup lightGroup; // 현재 조도 상태에 따른 led사용 여부, 조도 단계설정
    RadioButton step3Button;
   EditText hopeTempText; // 에어컨 희망 온도 설정
    Button saveButton; // 저장 버튼
    RadioButton useRadio; // 사용 라디오 버튼
    RadioButton useNotRadio; // 사용 안함 라디오 버튼
    boolean colorCheck = false; // led 색깔 입력 확인

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_setting);
        IRregisterButton = (Button)findViewById(R.id.IRregisterButton);

        saveButton = (Button)findViewById(R.id.saveButton); // 각 버튼을 가져옴
        redButton = (Button)findViewById(R.id.redButton);
        greenButton = (Button)findViewById(R.id.greenButton);
        blueButton = (Button)findViewById(R.id.blueButton);

        redValue = (EditText)findViewById(R.id.redValue);
        greenValue = (EditText)findViewById(R.id.greenValue);
        blueValue = (EditText)findViewById(R.id.blueValue);

        colorInsert = (Button)findViewById(R.id.colorInsert);
        colorView = (TextView)findViewById(R.id.colorView);

        useGroup = (RadioGroup)findViewById(R.id.useGroup);
        lightGroup = (RadioGroup)findViewById(R.id.lightGroup);
        step3Button = (RadioButton)findViewById(R.id.step3Button);
        useRadio = (RadioButton)findViewById(R.id.useRadio);
        useNotRadio = (RadioButton)findViewById(R.id.useNotRadio);

        hopeTempText = (EditText)findViewById(R.id.hopeTempText);

        step3Button.setChecked(true);
        hopeTempText.setEnabled(false); // 초기 입력불가능하도록 설정
        hopeTempText.setBackgroundColor(getResources().getColor(R.color.colorGray));

        IRregisterButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), IRregisterActivity.class);
                startActivity(intent);
            }
        });

        redButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { // LED 색깔 설정
                r = 255;
                g = 0;
                b = 0;
                redValue.setText(r+"");
                greenValue.setText(g+"");
                blueValue.setText(b+"");
                colorView.setBackgroundColor(Color.rgb(r, g, b));
            }
        });

        greenButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                r = 0;
                g = 255;
                b = 0;
                redValue.setText(r+"");
                greenValue.setText(g+"");
                blueValue.setText(b+"");
                colorView.setBackgroundColor(Color.rgb(r, g, b));
            }
        });

        blueButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                r = 0;
                g = 0;
                b = 255;
                redValue.setText(r+"");
                greenValue.setText(g+"");
                blueValue.setText(b+"");
                colorView.setBackgroundColor(Color.rgb(r, g, b));
            }
        });


        colorInsert.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { // 사용자 지정 색깔 입력 버튼

                if(redValue.getText().toString().equals("") || greenValue.getText().toString().equals("") || blueValue.getText().toString().equals("")) // 값이 하나라도 없는 경우 예외처리
                {

                    AlertDialog.Builder builder = new AlertDialog.Builder(SettingActivity.this);
                    dialog = builder.setMessage("모든 값을 입력해주세요.")
                            .setNegativeButton("확인", null)
                            .create();
                    dialog.show();
                 }else if(Integer.parseInt(redValue.getText().toString()) > 255 || Integer.parseInt(greenValue.getText().toString()) > 255 || Integer.parseInt(blueValue.getText().toString()) >255) // 255를 넘는경우 예외처리
                 {
                     AlertDialog.Builder builder = new AlertDialog.Builder(SettingActivity.this);
                     dialog = builder.setMessage("255이하의 정수만 입력해주세요.")
                             .setNegativeButton("확인", null)
                             .create();
                     dialog.show();
                }else
                {
                    r = Integer.parseInt(redValue.getText().toString());
                    g = Integer.parseInt(greenValue.getText().toString());
                    b = Integer.parseInt(blueValue.getText().toString());

                    Log.e("r => "+ r, "r => ");
                    Log.e("g => "+ g, "g => ");
                    Log.e("b => "+ b, "b => ");
                    colorView.setBackgroundColor(Color.rgb(r, g, b)); // 선택한 색깔 출력


                }
            }
        });

        useGroup.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup radioGroup, int i) {
                RadioButton airuseButton = (RadioButton)findViewById(i); // 현재 선택된 라디오버튼 받아옴
                if(airuseButton.getText().toString().equals("사용")) // 사용버튼에 선택된 경우 입력가능하도록 변경
                {
                    hopeTempText.setEnabled(true);
                    hopeTempText.setBackgroundColor(getResources().getColor(R.color.colorWhite));

                }else{ // 사용 안함 버튼에 선택된 경우 입력 불가능하도록 설정
                    hopeTempText.setEnabled(false);
                    hopeTempText.setBackgroundColor(getResources().getColor(R.color.colorGray));
                    airconThreshold = 0;
                }

            }
        });



        lightGroup.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() { // 조도 라디오 버튼에 대한 이벤트처리
            @Override
            public void onCheckedChanged(RadioGroup radioGroup, int i) {

                RadioButton lightButton = (RadioButton)findViewById(i); // 현재 선택된 라디오버튼 받아옴
                String light = lightButton.getText().toString();

                ledThreshold = Integer.parseInt(light.substring(0, 1)); // 선택된 단계의 숫자만 정수형으로 변환하여 저장
                Log.e("light => "+ light, "light => ");
                Log.e("ledThreshold => "+ ledThreshold, "ledThreshold => ");

            }
        });

        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { // 저장 버튼 리스너
                if(redValue.getText().toString().equals("") || greenValue.getText().toString().equals("") || blueValue.getText().toString().equals("")){ // 색깔이 입력안된경우 예외처리
                    AlertDialog.Builder builder = new AlertDialog.Builder(SettingActivity.this);
                    dialog = builder.setMessage("LED 색을 지정해주세요.")
                            .setNegativeButton("확인", null)
                            .create();
                    dialog.show();
                }else {
                    if (hopeTempText.getText().toString().equals("") && useRadio.isChecked()) { // 에어컨 온도 자동조절을 사용한다고 하였으나 값을 입력하지 않은경우 예외처리
                        AlertDialog.Builder builder = new AlertDialog.Builder(SettingActivity.this);
                        dialog = builder.setMessage("에어컨 설정값을 입력해주세요.")
                                .setNegativeButton("확인", null)
                                .create();
                        dialog.show();
                    } else {
                        if (useNotRadio.isChecked()) {
                            airconThreshold = 0;
                            sendRequest();
                        } else {
                            if (Integer.parseInt(hopeTempText.getText().toString()) < 16 || Integer.parseInt(hopeTempText.getText().toString()) > 27) { // 에어컨 가용온도 초과시 예외처리
                                AlertDialog.Builder builder = new AlertDialog.Builder(SettingActivity.this);
                                dialog = builder.setMessage("16~27의 온도를 입력해주세요.")
                                        .setNegativeButton("확인", null)
                                        .create();
                                dialog.show();
                            } else {
                                airconThreshold = Integer.parseInt(hopeTempText.getText().toString());
                                Log.e("airconThreshold => " + airconThreshold, "airconThreshold => ");
                                sendRequest();
                            }

                        }


                    }
                }


            }
        });



        if(AppHelper.requestQueue == null){
            //리퀘스트큐 생성 (MainActivit가 메모리에서 만들어질 때 같이 생성이 될것이다.
            AppHelper.requestQueue = Volley.newRequestQueue(getApplicationContext());
        }


    }

    public void sendRequest(){
        String url = "http://kyu9341.pythonanywhere.com/uleung/settings/"; // 세팅 테이블이 있는 url

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
                        AlertDialog.Builder builder = new AlertDialog.Builder(SettingActivity.this);
                        dialog = builder.setMessage("전송 성공.")
                                .setPositiveButton("확인", new DialogInterface.OnClickListener() { // 확인버튼을 누른경우 finish
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        finish();
                                    }
                                })
                                .create();
                        dialog.show();

                    } else {
                        AlertDialog.Builder builder = new AlertDialog.Builder(SettingActivity.this);
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

                params.put("ledRed", r +""); // 각 값들을 키값에 담아 서버에 전송
                params.put("ledGreen", g+"");
                params.put("ledBlue", b+"");
                params.put("ledThreshold", ledThreshold+"");
                params.put("airconThreshold", airconThreshold+"");


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
    @Override
    protected void onStop(){ //
        super.onStop();
        if(dialog != null)
        {
            dialog.dismiss();
            dialog = null;
        }

    }

}
