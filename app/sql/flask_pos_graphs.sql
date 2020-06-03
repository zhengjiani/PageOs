INSERT INTO flask_pos.graphs (id, pagename, pog) VALUES (1, 'PetClinic_page', '{''HomePage'': {''goto_Veter'': ''VeterPage'', ''goto_register'': ''RegisterPage'', ''goto_search'': ''FindPage''}, ''FindPage'': {''goto_detail_page'': ''DetailPage''}, ''RegisterPage'': {''regist_owner'': ''FindPage''}, ''DetailPage'': {''goto_add_pet'': ''AddNewPetPage'', ''goto_edit'': ''EditOwnerPage'', ''goto_edit_pet'': ''PetPage'', ''goto_pet'': ''PetPage'', ''goto_visit'': ''AddNewVisitPage''}, ''EditOwnerPage'': {''edit_info'': ''DetailPage''}, ''AddNewPetPage'': {''add_new_pet'': ''DetailPage''}, ''PetPage'': {''edit_pet'': ''DetailPage''}, ''AddNewVisitPage'': {''add_visit'': ''DetailPage''}, ''VeterPage'': {}}
');
INSERT INTO flask_pos.graphs (id, pagename, pog) VALUES (2, 'pageKit_page', '{''DashboardPage'': {''add_feed'': ''DashboardPage'', ''add_location'': ''DashboardPage'', ''add_user'': ''DashboardPage'', ''delete_loc'': ''DashboardPage'', ''delete_user_feed'': ''DeleteItemPage'', ''edit_feed'': ''DashboardPage'', ''edit_location'': ''DashboardPage'', ''edit_user'': ''DashboardPage'', ''go_edit_user'': ''AddEditUserPage'', ''go_site'': ''PagesPage'', ''go_users'': ''UserListPage'', ''goto_content'': ''AddEditPagePage''}, ''AddEditUserPage'': {''add_user'': ''AddEditUserPage'', ''edit_user'': ''AddEditUserPage'', ''goto_roles'': ''RolesPage'', ''goto_setting'': ''UserSettingPage'', ''goto_user_list'': ''UserListPage''}, ''PagesPage'': {''delete_link'': ''PagesPage'', ''delete_pages'': ''PagesPage'', ''edit_link'': ''AddEditLinkPage'', ''move_all_pages'': ''PagesPage'', ''publish_pages'': ''PagesPage'', ''unpublish_pages'': ''PagesPage''}, ''UserListPage'': {''activate_user'': ''UserListPage'', ''block_user'': ''UserListPage'', ''delete_user'': ''DeleteItemPage''}, ''SignInPage'': {''sign_in'': ''DashboardPage''}, ''AddEditLinkPage'': {''add_edit_meta'': ''SelectImagePage'', ''add_link'': ''AddEditLinkPage'', ''add_link_access'': ''AddEditLinkPage'', ''go_dashboard'': ''DashboardPage'', ''select_url'': ''SelectLinkPage''}, ''AddEditLoginPage'': {''add_details'': ''AddEditLoginPage'', ''add_details_access'': ''AddEditLoginPage'', ''go_dashboard'': ''DashboardPage'', ''restrict_visible'': ''AddEditLoginPage'', ''select_login'': ''SelectLinkPage'', ''select_logout'': ''SelectLinkPage''}, ''AddEditMenuPage'': {''add_edit_menu'': ''AddEditMenuPage'', ''add_edit_menu_access'': ''AddEditMenuPage'', ''add_visible_link'': ''AddEditMenuPage''}, ''AddEditTextPage'': {''add_edit_text'': ''AddEditTextPage'', ''add_edit_text_access'': ''AddEditTextPage''}, ''PermissionsPage'': {''operate_user_role'': ''PermissionsPage''}, ''RolesPage'': {''add_user_role'': ''AddEditItemPage'', ''delete_user_role'': ''DeleteItemPage'', ''edit_user_role'': ''AddEditItemPage'', ''operate_user_roles'': ''RolesPage''}, ''UserSettingPage'': {''change_settings'': ''SelectLinkPage'', ''save_settings'': ''UserSettingPage''}, ''WidgetsPage'': {''add_login'': ''AddEditLoginPage'', ''add_munu'': ''AddEditMenuPage'', ''add_text'': ''AddEditTextPage'', ''copy_widgets'': ''WidgetsPage'', ''delete_widgets'': ''WidgetsPage'', ''edit_login'': ''AddEditLoginPage'', ''edit_menu'': ''AddEditMenuPage'', ''edit_text'': ''AddEditTextPage'', ''go_Dashboard'': ''DashboardPage'', ''publish_widgets'': ''WidgetsPage'', ''unpublish_widgets'': ''WidgetsPage''}, ''AddEditPagePage'': {''add_edit'': ''AddEditPagePage'', ''add_edit_access'': ''AddEditPagePage'', ''add_edit_meta'': ''SelectItemPage''}}
');
INSERT INTO flask_pos.graphs (id, pagename, pog) VALUES (3, 'phoenix_page', '{''BoardsPage'': {''add_new_board'': ''BoardsPage'', ''goto_board_list'': ''BoardsListPage'', ''sign_out'': ''LoginPage'', ''view_all_boards'': ''BoardsPage''}, ''BoardsListPage'': {''add_new_card'': ''BoardsListPage'', ''add_new_list'': ''BoardsListPage'', ''add_new_member'': ''BoardsListPage'', ''goto_card'': ''CardDetails'', ''open_new_form'': ''BoardsListPage'', ''update_list'': ''BoardsListPage''}, ''LoginPage'': {''goto_signup'': ''SignUpPage'', ''login'': ''BoardsPage''}, ''SignUpPage'': {''goto_login'': ''LoginPage'', ''sign_up'': ''BoardsPage''}}
');