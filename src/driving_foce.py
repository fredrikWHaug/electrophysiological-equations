from utils import driving_force

if __name__ == '__main__':

    v_rest = -65
    v_2 = -50
    v_3 = -10
    v_4 = -10
    v_5 = -75

    e_na = 60
    e_k  = -80

    df_1 = driving_force(v_rest, e_na, e_k, 1)
    df_2 = driving_force(v_2, e_na, e_k, 2)
    df_3 = driving_force(v_3, e_na, e_k, 3)
    df_4 = driving_force(v_4, e_na, e_k, 4)
    df_5 = driving_force(v_5, e_na, e_k, 5)

    print(df_1)
    print(df_2)
    print(df_3)
    print(df_4)
    print(df_5)
