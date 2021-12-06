import scipy.io as io


def load_bfm_model(matFilePath):
    print('BFM: Loading model file...')
    return io.loadmat(matFilePath)  # '01_MorphableModel.mat'


def load_bfm_attributes():
    print('BFM: Loading attributes file...')
    return io.loadmat('../04_attributes.mat')


def output_shape(shape, f):
    shape = shape.T[0]

    for i in range(0, len(shape), 3):
        f.write('v {} {} {}\n'.format(
            shape[i], shape[i + 1], shape[i + 2]
        )
        )


def output_shape_and_texture(shape, texture, f):
    """
    Write shape in .obj format
    Args:
        shape(list): [[x_0, y_0, z_0], ..., [x_n, y_n, z_n]]
        f(filepointer): pointer to .obj file
    """
    shape = shape.T[0]
    texture = texture.T[0]

    for i in range(0, len(shape), 3):
        f.write('v {} {} {} {} {} {}\n'.format(
            shape[i], shape[i + 1], shape[i + 2],
            texture[i], texture[i + 1], texture[i + 2]
        )
        )


def output_triangles(triangles, f):
    """
    Write shape in .obj format
    Args:
        shape(list): [[x_0, y_0, z_0], ..., [x_n, y_n, z_n]]
        f(filepointer): pointer to .obj file
    """

    for i in range(0, len(triangles)):
        f.write('f {} {} {}\n'.format(
            triangles[i][2],
            triangles[i][1],
            triangles[i][0]
        ))


def output_triangles_new(triangles, f):
    """
    Write shape in .obj format
    Args:
        shape(list): [[x_0, y_0, z_0], ..., [x_n, y_n, z_n]]
        f(filepointer): pointer to .obj file
    """

    for i in range(0, len(triangles)):
        f.write('f {} {} {}\n'.format(
            int(triangles[i][1]),
            int(triangles[i][2]),
            int(triangles[i][0])
        ))


def save_to_obj(shape, texture, triangles, filename):
    with open(filename, 'w') as f:
        output_shape_and_texture(shape, texture, f)
        output_triangles(triangles, f)


def main():
    # dmm = load_bfm_model('01_MorphableModel.mat')
    dmm = load_bfm_model('MICCFlorence/BFM/BFM_model_front.mat')

    # with open('bfm_model.obj', 'w') as f:
    #     # output_shape_and_texture(dmm['shapeMU'], dmm['texMU'], f)
    #     output_shape(dmm['shapeMU'], f)
    #     output_triangles(dmm['tl'], f)

    with open('MICCFlorence/BFM/bfm_model_front.obj', 'w') as f:
        # output_shape_and_texture(dmm['shapeMU'], dmm['texMU'], f)
        output_shape(dmm['meanshape'].reshape(-1, 1), f)
        output_triangles_new(dmm['tri'], f)


if __name__ == '__main__':
    main()
