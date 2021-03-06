# ***************************************************************************************************
# This file holds the values of the global variables, which are needed throughout the operation
# ***************************************************************************************************
import numpy as np

# ===================================
# Database Variables
# ===================================
XRANGE = np.array([0, 19])
YRANGE = np.array([0, 19])

XQUANTIZE = 2500
YQUANTIZE = 2500

TRANSFORM_NORM = 0.5
IMG_CHANNELS   = 1

# ---logdir for saving the database ---
SAVE_PATH_DB = './database.pth'
# ---logdir for saving the network ----
SAVE_PATH_NET = './trained_nn.pth'
# -------------- paths --------------
PATH          = 'C:\\Users\\tomer\\Documents\\MATLAB\\csv_files\\grid_size_2500_2500\\corner_1450'
# \corner_1450_db_trunc.csv'  # \corner_1450_db_15p9k.csv'  # corner_1450_10k.csv'
PATH_DATABASE = '..\\..\\databases\\corner_1450_db_15p9k.csv'
PATH_LOGS     = 'C:\\Users\\TomerG\\PycharmProjects\\THESIS_TG\\results'
# ==================================
# Flow Control Variables
# ==================================
gather_DB = False
train     = True

# ============================================================
# Global variables of the net
# ============================================================
# --------------------------------------------------------
# Hyper parameters
# --------------------------------------------------------
BETA             = 1        # the KL coefficient in the cost function
EPOCH_NUM        = 300
LR               = 3e-4     # learning rate
MOM              = 0.9      # momentum update
NORM_FACT        = 64458    # output normalization factor - mean sensitivity
BATCH_SIZE       = 32
LATENT_SPACE_DIM = 50       # number of dimensions in the latent space
INIT_WEIGHT_MEAN = 0
INIT_WEIGHT_STD  = 0.02
# --------------------------------------------------------
# Encoder topology
# --------------------------------------------------------
"""
Encoder input: 2500 X 2500
conv1: 2500 --> 100
conv2: 100  --> 100
pool1: 100  --> 50
conv3: 50   --> 50
pool2: 50   --> 25
conv4: 25   --> 24
pool3: 24   --> 12
conv5: 10   --> 10
conv6: 10   --> 8
pool4: 8    --> 4
conv7: 4    --> 1

"""
ENCODER_LAYER_DESCRIPTION = {0: 'conv',
                             1: 'conv',
                             2: 'pool',
                             3: 'conv',
                             4: 'pool',
                             5: 'conv',
                             6: 'pool',
                             7: 'conv',
                             8: 'conv',
                             9: 'pool',
                             10: 'conv',
                             11: 'linear',
                             12: 'linear',
                             13: 'linear last',
                             }
# Number of filters in each filter layer
ENCODER_FILTER_NUM       = [1,  # INPUT, do not change
                            6,   # first layer
                            16,  # second layer
                            16,  # third layer
                            16,  # fourth layer
                            16,  # fifth layer
                            32,  # sixth layer
                            64,  # seventh layer
                            ]
# Filter sizes for each filter layer
ENCODER_KERNEL_SIZE      = [25,  # first layer
                            5,  # second layer
                            5,  # third layer
                            4,  # fourth layer
                            3,  # fifth layer
                            3,  # sixth layer
                            4,  # seventh layer
                            ]
# Stride values of the convolution layers
ENCODER_STRIDES          = [25,  # first layer
                            1,  # second layer
                            1,  # third layer
                            1,  # fourth layer
                            1,  # fifth layer
                            1,  # sixth layer
                            1,  # seventh layer
                            ]
# Padding values of the convolution layers
ENCODER_PADDING          = [0,  # first layer
                            2,  # second layer
                            2,  # third layer
                            1,  # fourth layer
                            0,  # fifth layer
                            0,  # sixth layer
                            0,  # seventh layer
                            ]
# Max pool size
ENCODER_MAX_POOL_SIZE    = [2,  # first max-pool
                            2,  # second max-pool
                            2,  # third max-pool
                            2,  # fourth max-pool
                            ]
# FC layer sizes
ENCODER_FC_LAYERS = [150,
                     150,
                     2 * LATENT_SPACE_DIM,
                    ]

# --------------------------------------------------------
# Dense Encoder topology
# --------------------------------------------------------
DENSE_ENCODER_LAYER_DESCRIPTION = {0: 'conv',
                                   1: 'dense',
                                   2: 'transition',
                                   3: 'dense',
                                   4: 'transition',
                                   5: 'dense',
                                   6: 'transition',
                                   7: 'dense',
                                   8: 'transition',
                                   9: 'dense',
                                   10: 'transition',
                                   11: 'linear',
                                   12: 'linear',
                                   13: 'linear last',
                                   }
DENSE_INIT_CONV_LAYER = [1,   # In channels
                         6,   # Out channels
                         25,  # Kernel size
                         25,  # Stride
                         0]   # Padding
# Growth rates for the dense blocks
DENSE_GROWTH_RATES = [40,
                      40,
                      40,
                      40,
                      40,
                      ]
# Depth of the dense layers
DENSE_DEPTHS = [5,
                5,
                5,
                5,
                5,
                ]
# Reduction rates for the transition blocks
DENSE_REDUCTION_RATES = [0.5,
                         0.5,
                         0.5,
                         0.5,
                         0.5,
                         ]
# Filter sizes for each filter layer
DENSE_ENCODER_KERNEL_SIZE      = [3,  # first layer
                                  3,  # second layer
                                  3,  # third layer
                                  3,  # fourth layer
                                  3,  # fifth layer
                                  ]
# Stride values of the convolution layers
DENSE_ENCODER_STRIDES          = [1,  # first layer
                                  1,  # second layer
                                  1,  # third layer
                                  1,  # fourth layer
                                  1,  # fifth layer
                                  ]
# Padding values of the convolution layers
DENSE_ENCODER_PADDING          = [1,  # first layer
                                  1,  # second layer
                                  1,  # third layer
                                  1,  # fourth layer
                                  1,  # fifth layer
                                  ]
# Max pool size
DENSE_ENCODER_MAX_POOL_SIZE    = [2,  # first max-pool
                                  2,  # second max-pool
                                  2,  # third max-pool
                                  2,  # fourth max-pool
                                  2,  # fifth max-pool
                                  ]
# FC layer sizes
DENSE_ENCODER_FC_LAYERS = [150,
                           150,
                           2 * LATENT_SPACE_DIM,
                           ]
# --------------------------------------------------------
# Decoder topology
# --------------------------------------------------------
"""
Decoder input: 2500 X 2500
conv1: 2500 --> 100
DECODER
"""
DECODER_LAYER_DESCRIPTION = {0: 'linear',
                             1: 'linear',
                             2: 'linear',
                             3: 'linear',
                             4: 'linear last',
                             }
# FC layer sizes
DECODER_FC_LAYERS = [250,
                     150,
                     100,
                     25,
                     1,
                     ]
