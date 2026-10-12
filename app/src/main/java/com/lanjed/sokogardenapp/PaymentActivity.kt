package com.lanjed.sokogardenapp

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.bumptech.glide.Glide
import com.loopj.android.http.RequestParams

class PaymentActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_payment)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }


//        receive/retrieve extra data from the product adapter
        val productName = intent.getStringExtra("product_name")
        val productCost = intent.getIntExtra("product_cost", 0)
        val productDescription = intent.getStringExtra("product_description")
        val productImage = intent.getStringExtra("product_photo")

//        find the views relative to the extra data from product adapter
        val txtName: TextView = findViewById(R.id.txtProductName)
        val txtCost: TextView = findViewById(R.id.txtProductCost)
        val txtDescription: TextView = findViewById(R.id.txtProductDescription)
        val imageProduct: ImageView = findViewById(R.id.txtProductPhoto)

//        find views for payment processing
        val btnPay: Button = findViewById(R.id.pay)
        val editPhone: EditText = findViewById(R.id.txtPhone)

//        display information coming from the product adapter
        txtName.text = productName
        txtCost.text = "ksh $productCost"
        txtDescription.text = productDescription

//        load product image using glide
        val imageUrl = "https://jeddy.alwaysdata.net/static/images/$productImage"
        Glide.with(this)
            .load(imageUrl)
            .placeholder(R.drawable.ic_launcher_background)
            .error(R.drawable.ic_launcher_background)
            .into(imageProduct)


//        handle payment button click
        btnPay.setOnClickListener {
            val phoneNumber = editPhone.text.toString().trim()
            if (phoneNumber.isEmpty())
            {
                editPhone.error = "Please enter your phone number again"
                editPhone.requestFocus()
                return@setOnClickListener
            }

            val api = "https://jeddy.alwaysdata.net/api/mpesa_payment"

            val data = RequestParams()
            data.put("amount", productCost)
            data.put("phone", phoneNumber)

            val helper = ApiHelper(applicationContext)
            helper.post(api, data)
        }
    }
}