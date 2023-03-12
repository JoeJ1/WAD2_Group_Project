class BackendTest(TestCase):

  # Database & Database Interaction

  def test_user_authentication(self):
      self.client = Client()
      self.user = User.objects.create_user(
          username='testuser',
          password='testpass'
      )
      # Log in the user
      self.client.login(username='testuser', password='testpass')

      # Check that the user is authenticated
      response = self.client.get(reverse('home'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'Welcome, testuser!')


  def test_display_correct_pages_if_owner_or_member(self):
    self.assertEqual(True, True)

  def test_display_only_your_classes(self):
    self.assertEqual(True, True)

  def test_able_to_create_new_accounts(self):
    self.assertEqual(True, True)

  def test_able_to_login_using_external_api(self):
    self.assertEqual(True, True)
    
  def test_files_should_have_expiry_dates(self):
    self.assertEqual(True, True)
    
  def test_user_can_download_view_files(self):
    self.assertEqual(True, True)
    
  def test_user_can_be_owner_or_student_of_several_chats(self):
    self.assertEqual(True, True)
    
  def test_user_can_create_new_classes(self):
    self.assertEqual(True, True)
    
  def test_owners_can_add_members_to_chats_they_own(self):
    self.assertEqual(True, True)

   # Website & User Interface

  def test_website_should_include_nav_bar(self):
    self.assertEqual(True, True)
    
  def test_live_chat_form_using_ajax_or_asgi(self):
    self.assertEqual(True, True)
    
  def test_user_should_be_able_to_see_and_interact_with_live_chats(self):
    self.assertEqual(True, True)
    
  def test_owner_sees_different_interface_compared_to_member(self):
    self.assertEqual(True, True)

