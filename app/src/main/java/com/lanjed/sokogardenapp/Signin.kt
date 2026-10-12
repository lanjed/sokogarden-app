package com.lanjed.sokogardenapp

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.loopj.android.http.RequestParams

class Signin : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_signin)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

//        extract values from views
        val email = findViewById<EditText>(R.id.email)
        val password = findViewById<EditText>(R.id.password)
        val signin = findViewById<Button>(R.id.signin_button)

//        submit details to log in implementation
        signin.setOnClickListener {
            val api = "https://jeddy.alwaysdata.net/api/signin"

            val data = RequestParams()
            data.put("email", email.text.toString())
            data.put("password", password.text.toString())

            val helper = ApiHelper(applicationContext)
            helper.post_login(api,data)
        }

    }
}