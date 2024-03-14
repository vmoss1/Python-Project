const POST_IMAGE = '/post-image'


export const createImage = (post) => async (dispatch) => {
    const response = await fetch(`/images/new`, {
      method: "POST",
    //   headers: {
    //     'Accept': 'application/json',
    //     "Content-Type": "application/json",
    //   },
      body: post
    });

    if (response.ok) {
        const { resPost } = await response.json();
        dispatch(addPost(resPost));
    } else {
        console.log("There was an error making your post!")
    }
};
