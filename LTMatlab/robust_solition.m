function [ distribution_matrix_prob ] = robust_solition( packet_num )
    %理想孤波分布
    
    p_ideal = zeros(1,packet_num);
    p_ideal(1) = 1/packet_num;
    for i = 2:packet_num
        p_ideal(i) = 1/(i*(i-1));
    end

%     figure(2)
%     bar(p_ideal)
%     xlabel('Degree')
%     ylabel('Frequency')
%     axis([0 50 0 0.5])
%     title('理想孤波分布')

    %鲁棒孤波分布
    %参数
    c = 0.05;
    delta = 0.05; %保证译码成功概率为  1-delta
    p_robust = p_ideal;
    

    R = c*log(packet_num/delta)*sqrt(packet_num);
    degree_max = round(packet_num / R); %度数上限
    p = zeros(1,degree_max);  %度分布概率矩阵
    
       
    for i = 1:degree_max-1
        p(i) = R/(i*packet_num);
    end
    
    p(degree_max) = R*log(R/delta)/packet_num;
    
    %鲁棒孤波分布为p与p_ideal相加然后归一化
    for i = 1:degree_max
        p_robust(i) = p_ideal(i) + p(i);
    end

    p_robust = p_robust/sum(p_robust);
    max_num = find(p_robust > (0.1/packet_num), 1, 'last' );
    distribution_matrix_prob = p_robust(1:max_num);
    temp_sum = sum(distribution_matrix_prob);
    distribution_matrix_prob = distribution_matrix_prob .* (1/temp_sum);
    real_degree_max = length(distribution_matrix_prob);
%     figure(3)
%     bar(distribution_matrix_prob)
%     xlabel('Degree')
%     ylabel('Frequency')
%     title('鲁棒孤波分布')
%     axis([0 50 0 0.5])
end

