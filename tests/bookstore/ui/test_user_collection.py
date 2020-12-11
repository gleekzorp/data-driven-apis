
def test_user_can_remove_book_from_their_collection(py, user_with_books, login_seam, profile):
    login_seam('/profile')
    profile.remove_book_by_name('Git Pocket Guide')
    assert py.should().not_contain('Git Pocket Guide')
