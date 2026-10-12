package com.lanjed.sokogardenapp

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.loopj.android.http.RequestParams

class Signup : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_signup)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

//        form data values from signup xml
        val username = findViewById<EditText>(R.id.username)
        val password = findViewById<EditText>(R.id.password)
        val phone = findViewById<EditText>(R.id.phone)
        val email = findViewById<EditText>(R.id.email)

        val signup_button = findViewById<Button>(R.id.signup_button)

//        signup registration implementation
        signup_button.setOnClickListener {
            val api = "https://jeddy.alwaysdata.net/api/signup"


            val data = RequestParams()
            data.put("username", username.text.toString())
            data.put("password", password.text.toString())
            data.put("email", email.text.toString())
            data.put("phone", phone.text.toString())

            val helper = ApiHelper(applicationContext)
            helper.post(api, data)
        }


    }
}