require 'test_helper'

class MainControllerTest < ActionController::TestCase
  test "should get hellp" do
    get :hellp
    assert_response :success
  end

end
