from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserRegister, UserLogin, UserResponse
from app.crud.user import get_user_by_email, create_user
from app.core.dependencies import get_db
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db, user)


@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)

    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.id}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "id":db_user.id,
        "name":db_user.name
    }

#
# @router.post("/login")
# def login_user(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(get_db)
# ):
#     # Swagger sends username & password (form-data)
#     email = form_data.username   # treat username as email
#     password = form_data.password
#     # print(email, password)
#     db_user = get_user_by_email(db, email)
#     # print(db_user)
#     if not db_user or not verify_password(password, db_user.password_hash):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid email or password"
#         )
#
#     access_token = create_access_token(
#         data={"sub": str(db_user.id)}  # keep as string (JWT best practice)
#     )
#
#     return {
#         "access_token": access_token,
#         "token_type": "bearer",
#         "id": db_user.id,
#         "name": db_user.name
#     }
