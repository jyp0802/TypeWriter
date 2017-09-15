class MainController < ApplicationController
  def hello
    
  end
  def post_input
    
    #form_data = {
    #    "input" => @email_to,
    #}
    #url = "https://api.venmo.com/v1/payments"
    #request = Net::HTTP::Post.new(url, form_data)

    #response = http.request(request)
    redirect_to "image/output"
  end
end
