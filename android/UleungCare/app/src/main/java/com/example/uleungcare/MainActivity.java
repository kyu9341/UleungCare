package com.example.uleungcare;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    Button cctvButton;
    Button controllerButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        cctvButton = (Button)findViewById(R.id.cctvButton);
        controllerButton = (Button)findViewById(R.id.controllerButton);

        cctvButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

//                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.naver.com/"));

                Intent intent = new Intent(getApplicationContext(), CCTVActivity.class);
                startActivity(intent);
            }
        });

        controllerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), ControllerActivity.class);
                startActivity(intent);
            }
        });

    }
}
